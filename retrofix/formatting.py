##############################################################################
#
#    Copyright (C) 2013 NaN Projectes de Programari Lliure, S.L.
#                            http://www.NaN-tic.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

def format_string(text, length, fill=' ', align='<'):
    """
    Formats the string into a fixed length ASCII (iso-8859-1) record.

    Original code by: Pexego
    """

    if not text:
        return fill*length

    #
    # String uppercase
    #
    text = text.upper()

    #
    # Turn text (probably unicode) into an ASCII (iso-8859-1) string
    #
    if isinstance(text, (unicode)):
        ascii_string = text.encode('iso-8859-1', 'ignore')
    else:
        ascii_string = str(text or '')
    # Cut the string if it is too long
    if len(ascii_string) > length:
        ascii_string = ascii_string[:length]
    # Format the string
    #ascii_string = '{0:{1}{2}{3}s}'.format(ascii_string, fill, align, length) #for python >= 2.6
    if align == '<':
        ascii_string = str(ascii_string) + (length-len(str(ascii_string)))*fill
    elif align == '>':
        ascii_string = (length-len(str(ascii_string)))*fill + str(ascii_string)
    else:
        assert False, 'Wrong aling option. It should be < or >'

    # Sanity-check
    assert len(ascii_string) == length, (
            'Formatted string must match the given length')
    # Return string
    return ascii_string


def format_number(number, int_length, dec_length=0, include_sign=False):
    """
    Formats the number into a fixed length ASCII (iso-8859-1) record.

    :param number: Decimal value
    :param int_length: Number of digits to be used for the integer part
    :param dec_length: Number of digits to be used for the decimal part
    :param include_sign: Wether the sign should be added or not

    Original code by: Pexego
    """

    # TODO: Allow defining how the sign should be shown

    #
    # Separate the number parts (-55.23 => int_part=55, dec_part=0.23, sign='N')
    #
    if number == '':
        number = Decimal('0.0')

    sign = number > 0 and ' ' or 'N'
    number = abs(number)
    int_part = int(number)

    # Format the string
    ascii_string = ''
    if include_sign:
        ascii_string += sign

    if dec_length > 0:
        ascii_string += '%0*.*f' % (int_length+dec_length+1,dec_length, number)
        ascii_string = ascii_string.replace('.','')
    elif int_length > 0:
        ascii_string += '%.*d' % (int_length, int_part)

    assert (len(ascii_string) == (include_sign and 1 or 0) + int_length +
        dec_length), 'Formatted number must match the given length'

    return ascii_string
