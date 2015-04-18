__author__ = 'RanadeepPolavarapu'

import random
import string
import time
import datetime
import calendar
import re
import pytz


class Utils:

    """
    Created for personal use withn a few web projects.

    Created for use under Python 3+.
    """

    # Follows ISO 3166-2, http://en.wikipedia.org/wiki/ISO_3166-2.
    ISO_LOCALE_LANGUAGE_CODES = {
        'ia': 'Interlingua',
        'ik': 'Inupiak; Inupiaq',
        'am': 'Amharic',
        'km': 'Central Khmer; Cambodian',
        'wa': 'Walloon',
        'gn': 'Guarani',
        'hi': 'Hindi',
        'tl': 'Tagalog',
        'tk': 'Turkmen',
        'ca': 'Catalan',
        'iu': 'Inuktitut',
        'sn': 'Shona',
        'to': 'Tonga',
        'lu': 'Luba-Katanga',
        'kr': 'Kanuri',
        'yo': 'Yoruba',
        'uz': 'Uzbek',
        'ks': 'Kashmiri',
        'sq': 'Albanian',
        'sl': 'Slovenian',
        'be': 'Belarusian',
        'kk': 'Kazakh',
        'gl': 'Galician',
        'ug': 'Uighur',
        'bo': 'Tibetan',
        'af': 'Afrikaans',
        'fi': 'Finnish',
        'fo': 'Faroese',
        'ee': 'Éwé',
        'sw': 'Swahili',
        'gv': 'Manx',
        'zu': 'Zulu',
        'cr': 'Cree',
        'ro': 'Romanian',
        'ab': 'Abkhazian',
        'ng': 'Ndonga',
        'tw': 'Twi',
        'pa': 'Panjabi; Punjabi',
        'mi': 'Maori',
        'bh': 'Bihari',
        'lv': 'Latvian; Lettish',
        'mt': 'Maltese',
        'zh': 'Chinese',
        'ae': 'Avestan',
        'ne': 'Nepali',
        'ig': 'Igbo',
        'kv': 'Komi',
        'es': 'Spanish',
        'xh': 'Xhosa',
        'eo': 'Esperanto',
        'pi': 'Pali',
        'no': 'Norwegian',
        'kg': 'Kongo',
        'nb': 'Norwegian Bokmål',
        'si': 'Sinhala; Sinhalese',
        'ar': 'Arabic',
        'so': 'Somali',
        'tt': 'Tatar',
        'nl': 'Dutch',
        'or': 'Oriya',
        'da': 'Danish',
        'ps': 'Pashto; Pushto',
        'bi': 'Bislama',
        'ky': 'Kirghiz',
        'tr': 'Turkish',
        'ru': 'Russian',
        'ho': 'Hiri Motu',
        'eu': 'Basque',
        'bn': 'Bengali; Bangla',
        'su': 'Sundanese',
        'hr': 'Croatian',
        'ka': 'Georgian',
        've': 'Venda',
        'nd': 'Ndebele, North',
        'ff': 'Fulah',
        'nr': 'Ndebele, South',
        'fa': 'Persian',
        'io': 'Ido',
        'oc': 'Occitan; Provençal',
        'aa': 'Afar',
        'ha': 'Hausa',
        'jv': 'Javanese',
        'sa': 'Sanskrit',
        'ms': 'Malay',
        'dz': 'Dzongkha; Bhutani',
        'ht': 'Haitian; Haitian Creole',
        'kl': 'Kalaallisut; Greenlandic',
        'en': 'English',
        'sm': 'Samoan',
        'lo': 'Lao; Laotian',
        'mh': 'Marshallese',
        'sd': 'Sindhi',
        'he': 'Hebrew (formerly iw)',
        'ja': 'Japanese',
        'ki': 'Kikuyu; Gikuyu',
        'ii': 'Sichuan Yi; Nuosu',
        'li': 'Limburgish; Limburger; Limburgan',
        'hu': 'Hungarian',
        'la': 'Latin',
        'tg': 'Tajik',
        'cv': 'Chuvash',
        'co': 'Corsican',
        'ln': 'Lingala',
        'th': 'Thai',
        'bm': 'Bambara',
        'mn': 'Mongolian',
        'sv': 'Swedish',
        'nn': 'Norwegian Nynorsk',
        'lb': 'Letzeburgesch; Luxembourgish',
        'mg': 'Malagasy',
        'lg': 'Ganda',
        'yi': 'Yiddish (formerly ji)',
        'gd': 'Scottish Gaelic',
        'mo': 'Moldavian',
        'dv': 'Divehi; Maldivian',
        'te': 'Telugu',
        'om': '(Afan) Oromo',
        'fy': 'Western Frisian',
        'br': 'Breton',
        'kj': 'Kuanyama; Kwanyama',
        'sc': 'Sardinian',
        'cu': 'Church Slavic',
        'bg': 'Bulgarian',
        'kn': 'Kannada',
        'mr': 'Marathi',
        'sk': 'Slovak',
        'st': 'Sesotho; Sotho, Southern',
        'ta': 'Tamil',
        'ga': 'Irish',
        'el': 'Greek',
        'ti': 'Tigrinya',
        'wo': 'Wolof',
        'hz': 'Herero',
        'rw': 'Kinyarwanda',
        'is': 'Icelandic',
        'ko': 'Korean',
        'id': 'Indonesian (formerly in)',
        'ml': 'Malayalam',
        'ch': 'Chamorro',
        'ku': 'Kurdish',
        'gu': 'Gujarati',
        'ak': 'Akan',
        'kw': 'Cornish',
        'ba': 'Bashkir',
        'ce': 'Chechen',
        'de': 'German',
        'my': 'Burmese',
        'ay': 'Aymara',
        'cs': 'Czech',
        'mk': 'Macedonian',
        'tn': 'Tswana; Setswana',
        'lt': 'Lithuanian',
        'sg': 'Sango; Sangro',
        'ss': 'Swati; Siswati',
        'an': 'Aragonese',
        'sr': 'Serbian',
        'av': 'Avaric',
        'it': 'Italian',
        'fr': 'French',
        'na': 'Nauru',
        'cy': 'Welsh',
        'ur': 'Urdu',
        'hy': 'Armenian',
        'as': 'Assamese',
        'et': 'Estonian',
        'os': 'Ossetian; Ossetic',
        'rm': 'Romansh',
        'ie': 'Interlingue; Occidental',
        'rn': 'Rundi; Kirundi',
        'nv': 'Navajo; Navaho',
        'se': 'Northern Sami',
        'ty': 'Tahitian',
        'fj': 'Fijian; Fiji',
        'ts': 'Tsonga',
        'bs': 'Bosnian',
        'ny': 'Chichewa; Nyanja',
        'vo': 'Volapük; Volapuk',
        'pt': 'Portuguese',
        'vi': 'Vietnamese',
        'oj': 'Ojibwa',
        'uk': 'Ukrainian',
        'za': 'Zhuang',
        'qu': 'Quechua',
        'pl': 'Polish',
        'az': 'Azerbaijani'}

    ISO_LOCALE_COUNTRY_CODES = {
        'PL': 'Poland',
        'AI': 'Anguilla',
        'DJ': 'Djibouti',
        'PT': 'Portugal',
        'DE': 'Germany',
        'TD': 'Chad',
        'BL': 'Saint Barthelemy',
        'IN': 'India',
        'TL': 'Timor-Leste',
        'WF': 'Wallis and Futuna',
        'GI': 'Gibraltar',
        'MY': 'Malaysia',
        'BW': 'Botswana',
        'LT': 'Lithuania',
        'SD': 'Sudan',
        'TC': 'Turks and Caicos Islands',
        'SX': 'Sint Maarten (Dutch part)',
        'LU': 'Luxembourg',
        'KH': 'Cambodia',
        'AD': 'Andorra',
        'HM': 'Heard Island and McDonald Islands',
        'PN': 'Pitcairn',
        'GP': 'Guadeloupe',
        'BN': 'Brunei Darussalam',
        'IR': 'Iran, Islamic Republic of',
        'DZ': 'Algeria',
        'ZA': 'South Africa',
        'TJ': 'Tajikistan',
        'MD': 'Moldova, Republic of',
        'ZW': 'Zimbabwe',
        'LS': 'Lesotho',
        'BG': 'Bulgaria',
        'ET': 'Ethiopia',
        'FR': 'France',
        'SL': 'Sierra Leone',
        'HN': 'Honduras',
        'PE': 'Peru',
        'GD': 'Grenada',
        'EG': 'Egypt',
        'TW': 'Taiwan, Province of China',
        'GH': 'Ghana',
        'IS': 'Iceland',
        'PK': 'Pakistan',
        'KM': 'Comoros',
        'SB': 'Solomon Islands',
        'BQ': 'Bonaire, Sint Eustatius and Saba',
        'BJ': 'Benin',
        'KN': 'Saint Kitts and Nevis',
        'UY': 'Uruguay',
        'VN': 'Viet Nam',
        'EC': 'Ecuador',
        'ID': 'Indonesia',
        'SE': 'Sweden',
        'GY': 'Guyana',
        'IL': 'Israel',
        'AM': 'Armenia',
        'CL': 'Chile',
        'UG': 'Uganda',
        'VI': 'Virgin Islands, US',
        'RW': 'Rwanda',
        'KE': 'Kenya',
        'BH': 'Bahrain',
        'NO': 'Norway',
        'NR': 'Nauru',
        'SV': 'El Salvador',
        'GG': 'Guernsey',
        'PG': 'Papua New Guinea',
        'KI': 'Kiribati',
        'RU': 'Russian Federation',
        'RO': 'Romania',
        'MV': 'Maldives',
        'VU': 'Vanuatu',
        'PA': 'Panama',
        'LV': 'Latvia',
        'AO': 'Angola',
        'NA': 'Namibia',
        'BY': 'Belarus',
        'NG': 'Nigeria',
        'AF': 'Afghanistan',
        'GB': 'United Kingdom',
        'SA': 'Saudi Arabia',
        'GQ': 'Equatorial Guinea',
        'GA': 'Gabon',
        'EE': 'Estonia',
        'NC': 'New Caledonia',
        'MG': 'Madagascar',
        'MC': 'Monaco',
        'CZ': 'Czech Republic',
        'BE': 'Belgium',
        'MA': 'Morocco',
        'MF': 'Saint Martin (French part)',
        'SJ': 'Svalbard and Jan Mayen',
        'NP': 'Nepal',
        'LY': 'Libya',
        'CH': 'Switzerland',
        'BS': 'Bahamas',
        'CG': 'Congo',
        'MK': 'Macedonia, The Former Yugoslav Republic of',
        'TN': 'Tunisia',
        'NL': 'Netherlands',
        'JM': 'Jamaica',
        'HT': 'Haiti',
        'MU': 'Mauritius',
        'CK': 'Cook Islands',
        'CA': 'Canada',
        'ME': 'Montenegro',
        'DO': 'Dominican Republic',
        'SM': 'San Marino',
        'PF': 'French Polynesia',
        'NF': 'Norfolk Island',
        'CV': 'Cape Verde',
        'LB': 'Lebanon',
        'UZ': 'Uzbekistan',
        'CI': 'Côte dIvoire',
        'VG': 'Virgin Islands, British',
        'KZ': 'Kazakhstan',
        'RS': 'Serbia',
        'CC': 'Cocos (Keeling) Islands',
        'BI': 'Burundi',
        'US': 'United States',
        'SN': 'Senegal',
        'VE': 'Venezuela, Bolivarian Republic of',
        'FO': 'Faroe Islands',
        'NE': 'Niger',
        'EH': 'Western Sahara',
        'AE': 'United Arab Emirates',
        'TK': 'Tokelau',
        'KW': 'Kuwait',
        'CW': 'Curaçao',
        'NI': 'Nicaragua',
        'CF': 'Central African Republic',
        'MN': 'Mongolia',
        'JE': 'Jersey',
        'BR': 'Brazil',
        'HK': 'Hong Kong',
        'AQ': 'Antarctica',
        'TH': 'Thailand',
        'PM': 'Saint Pierre and Miquelon',
        'TM': 'Turkmenistan',
        'LA': 'Lao Peoples Democratic Republic',
        'BM': 'Bermuda',
        'BD': 'Bangladesh',
        'AL': 'Albania',
        'GE': 'Georgia',
        'TO': 'Tonga',
        'MM': 'Myanmar',
        'BO': 'Bolivia, Plurinational State of',
        'IE': 'Ireland',
        'WS': 'Samoa',
        'FK': 'Falkland Islands (Malvinas)',
        'YE': 'Yemen',
        'CN': 'China',
        'CX': 'Christmas Island',
        'SC': 'Seychelles',
        'JO': 'Jordan',
        'DM': 'Dominica',
        'BV': 'Bouvet Island',
        'LR': 'Liberia',
        'VA': 'Holy See (Vatican City State)',
        'SY': 'Syrian Arab Republic',
        'SG': 'Singapore',
        'MW': 'Malawi',
        'CD': 'Congo, The Democratic Republic of the',
        'BZ': 'Belize',
        'KY': 'Cayman Islands',
        'SK': 'Slovakia',
        'ML': 'Mali',
        'PW': 'Palau',
        'FJ': 'Fiji',
        'UA': 'Ukraine',
        'CY': 'Cyprus',
        'GM': 'Gambia',
        'DK': 'Denmark',
        'SH': 'Saint Helena, Ascension and Tristan da Cunha',
        'PR': 'Puerto Rico',
        'AS': 'American Samoa',
        'BF': 'Burkina Faso',
        'AR': 'Argentina',
        'TZ': 'Tanzania, United Republic of',
        'RE': 'Reunion',
        'AW': 'Aruba',
        'CM': 'Cameroon',
        'MR': 'Mauritania',
        'NU': 'Niue',
        'GT': 'Guatemala',
        'LI': 'Liechtenstein',
        'KR': 'Korea, Republic of',
        'SZ': 'Swaziland',
        'ES': 'Spain',
        'FM': 'Micronesia, Federated States of',
        'AZ': 'Azerbaijan',
        'FI': 'Finland',
        'OM': 'Oman',
        'NZ': 'New Zealand',
        'KG': 'Kyrgyzstan',
        'TV': 'Tuvalu',
        'AT': 'Austria',
        'MS': 'Montserrat',
        'GN': 'Guinea',
        'MX': 'Mexico',
        'GU': 'Guam',
        'TF': 'French Southern Territories',
        'MP': 'Northern Mariana Islands',
        'UM': 'United States Minor Outlying Islands',
        'CU': 'Cuba',
        'PH': 'Philippines',
        'PY': 'Paraguay',
        'JP': 'Japan',
        'IO': 'British Indian Ocean Territory',
        'IT': 'Italy',
        'TG': 'Togo',
        'IQ': 'Iraq',
        'LK': 'Sri Lanka',
        'AG': 'Antigua and Barbuda',
        'BT': 'Bhutan',
        'QA': 'Qatar',
        'SO': 'Somalia',
        'SI': 'Slovenia',
        'BA': 'Bosnia and Herzegovina',
        'LC': 'Saint Lucia',
        'SR': 'Suriname',
        'AU': 'Australia',
        'GF': 'French Guiana',
        'PS': 'Palestine, State of',
        'IM': 'Isle of Man',
        'HR': 'Croatia',
        'ER': 'Eritrea',
        'GW': 'Guinea-Bissau',
        'GR': 'Greece',
        'CO': 'Colombia',
        'VC': 'Saint Vincent and the Grenadines',
        'GL': 'Greenland',
        'AX': 'Aaland Islands',
        'TT': 'Trinidad and Tobago',
        'MZ': 'Mozambique',
        'ST': 'Sao Tome and Principe',
        'GS': 'South Georgia and the South Sandwich Islands',
        'KP': 'Korea, Democratic Peoples Republic of',
        'YT': 'Mayotte',
        'MQ': 'Martinique',
        'CR': 'Costa Rica',
        'SS': 'South Sudan',
        'MT': 'Malta',
        'MO': 'Macao',
        'HU': 'Hungary',
        'TR': 'Turkey',
        'MH': 'Marshall Islands',
        'ZM': 'Zambia',
        'BB': 'Barbados'}

    def __init__(self):
        pass

    @staticmethod
    def string_subtraction(a, b):
        return ''.join(a.rsplit(b))

    @staticmethod
    def list_subtraction(list_one, list_two):
        s = set(list_two)
        diff_list = [x for x in list_one if x not in s]
        return diff_list

    @staticmethod
    def random_id_generator(size, chars=string.ascii_letters + string.digits):
        """
        Useful to generate random IDs, strings, passwords, etc.

        Uses alphabetical chars, numerical chars, whitespace, and punctuation to generate as specified below.

        Available 'chars' argument:
            string.ascii_letters - string.ascii_lowercase + string.ascii_uppercase
            string.ascii_lowercase - 'abcdefghijklmnopqrstuvwxyz'
            string.ascii_uppercase - 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            string.digits - '0123456789'
            string.hexdigits - '0123456789abcdefABCDEF'
            string.octdigits - '01234567'
        """
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def reverse_id(id):
        """
        Provides a reverse/inverse result of the id(...) built-in function value.

        NOTE: id(...) is the equivalent to ANSI C's memory address.

        WARNING: Do NOT use id(...) as a encode and decoder. id(...) is unique to the session and doesn't
            provide a reliable solution for encoding and decoding values. Use actual Cryptography or
            a custom algorithm for encoding and decoding based on a key.

        Ex:
            >> id("foobar")
            4363612336
            >> reverse_id(4363612336)
            'foobar'
        """
        import ctypes
        return ctypes.cast(id, ctypes.py_object).value

    @staticmethod
    def random_color_hex():
        r = lambda: random.randint(0, 255)
        return '#%02X%02X%02X' % (r(), r(), r())

    @staticmethod
    def convert_timestamp_to_UTC_datetime(
            timestamp, time_format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.strptime(
            timestamp, time_format).replace(tzinfo=pytz.utc)

    @staticmethod
    def convert_timestamp_to_UTC_epoch(
            timestamp, time_format="%Y-%m-%d %H:%M:%S"):
        epoch = calendar.timegm(
            datetime.datetime.strptime(
                timestamp,
                time_format).utctimetuple())
        return epoch

    @staticmethod
    def convert_epoch_to_datetime(epoch, UTC=True, epoch_milliseconds=False):
        if epoch_milliseconds:
            epoch /= 1000

        if UTC:
            dt = datetime.datetime.utcfromtimestamp(
                epoch).replace(tzinfo=pytz.utc)
        else:
            dt = datetime.datetime.fromtimestamp(epoch)
        return dt

    @staticmethod
    def get_epoch():
        # Epoch/Unix time in UTC timezone. There is no such thing as epoch in
        # local timezone.
        return int(time.time())

    @staticmethod
    def convert_seconds_to_other_units_of_time(sec):
        minutes, seconds = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)
        return (weeks, days, hours, minutes, seconds)

    @staticmethod
    def _delete_keys_from_nested_dict(deletion_dict, delete_keys_list):
        """
        Auxiliary function to delete_keys_from_list_or_dict(...) function.

            deletion_dict - The dictionary on which you are performing deletion on.
                Type: dict

            delete_keys_list - A list of strings which represent the keys that need to be deleted.
                Type: list
        """
        if (isinstance(deletion_dict, dict)) or (
                isinstance(deletion_dict, list)):
            # Handle the case if the deletion_dict is a string, int, float,
            # etc.. - This case is to prevent errors when dict is a list of
            # primary data types and not of secondary data types list or dict.
            # This ensures the deletion_dict is of type secondary data type
            # (i.e. dict or list).
            for k in delete_keys_list:
                try:
                    # deletion_dict.pop(k, None)
                    del deletion_dict[k]
                except KeyError:
                    pass
            for v in deletion_dict.values():
                if isinstance(v, dict):
                    # Handle the cases in which value is a dict.
                    Utils._delete_keys_from_nested_dict(
                        v,
                        delete_keys_list)
                elif isinstance(v, list):
                    # Handle the cases in which value is a list with elements
                    # being dicts.
                    for dict_element in v:
                        if isinstance(dict_element, dict):
                            # Confirm that each element is a dict. If not,
                            # ignore and skip over it.
                            Utils._delete_keys_from_nested_dict(
                                dict_element,
                                delete_keys_list)
        return deletion_dict

    @staticmethod
    def delete_keys_from_list_or_dict(deletion_obj, delete_keys_list):
        if isinstance(deletion_obj, list):
            resultant_list = []
            for element in deletion_obj:
                result = Utils._delete_keys_from_nested_dict(
                    element,
                    delete_keys_list)
                resultant_list.append(result)
            return resultant_list
        else:
            return Utils._delete_keys_from_nested_dict(
                deletion_obj, delete_keys_list)

    @staticmethod
    def _rename_keys_from_nested_dict(
            renaming_dict, original_key, renamed_key):
        """
        Auxiliary function to rename_keys_from_list_or_dict(...) function.

            renaming_dict - The dictionary on which you are performing renaming action on.
                Type: dict

            original_key - The original key as a string. This is key that you want renamed.
                Type: str

            renamed_key - The new key as a string. This is key in which you want original_key renamed to a new key name.
                Type: str
        """
        if (isinstance(renaming_dict, dict)) or (
                isinstance(renaming_dict, list)):
            # Handle the case if the renaming_dict is a string, int, float,
            # etc.. - This case is to prevent errors when dict is a list of
            # primary data types and not of secondary data types list or dict.
            # This ensures the renaming_dict is of type secondary data type
            # (i.e. dict or list).
            try:
                # Renaming could be done in one step via pop reassign but this
                # is more visually clear to understand.
                renaming_dict[renamed_key] = renaming_dict[original_key]
                del renaming_dict[original_key]
            except KeyError:
                pass
            for v in renaming_dict.values():
                if isinstance(v, dict):
                    # Handle the cases in which value is a dict.
                    Utils._rename_keys_from_nested_dict(
                        v,
                        original_key,
                        renamed_key)
                elif isinstance(v, list):
                    # Handle the cases in which value is a list with elements
                    # being dicts.
                    for dict_element in v:
                        if isinstance(dict_element, dict):
                            # Confirm that each element is a dict. If not,
                            # ignore and skip over it.
                            Utils._rename_keys_from_nested_dict(
                                dict_element,
                                original_key,
                                renamed_key)
        return renaming_dict

    @staticmethod
    def rename_keys_from_list_or_dict(renaming_obj, original_key, renamed_key):
        if isinstance(renaming_obj, list):
            resultant_list = []
            for element in renaming_obj:
                result = Utils._rename_keys_from_nested_dict(
                    element,
                    original_key,
                    renamed_key)
                resultant_list.append(result)
            return resultant_list
        else:
            return Utils._rename_keys_from_nested_dict(
                renaming_obj, original_key, renamed_key)

    @staticmethod
    def remove_duplicates_from_list(sequence):
        # Uses f7 algorithm. f7 is the fastest algorithm for duplicate removal.
        # NOTE: This works perfectly for hashable data types. i.e.: Single lists.
        # This does NOT work for unhashable types (dicts).
        # See function below for unhashable type duplicate removal.
        seen = set()
        seen_add = seen.add
        return [x for x in sequence if not (x in seen or seen_add(x))]

    @staticmethod
    def remove_duplicates_from_list_of_dicts(l):
        # Used to remove duplicates from a list containing unhashable data types (i.e.: dict).
        # Used in our internals when we map out recent_games_map which is a
        # list of dicts to remove duplicates entered during the internal
        # update/register process.
        return [dict(t) for t in set([tuple(d.items()) for d in l])]

    @staticmethod
    def check_for_list_duplicates(l):
        # NOTE: This is for a list of hashable data types. For unhashable data
        # types see below function.
        return len(l) != len(set(l))

    @staticmethod
    def check_for_list_duplicates_with_unhashables(l):
        return len(l) != len([dict(t)
                              for t in set([tuple(d.items()) for d in l])])

    @staticmethod
    def chunker(seq, size):
        # A utility function that returns a generator object which is an
        # interable object. This function allows us to split a set (list, tuple)
        # into a an N number of subsets.
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    @staticmethod
    def group_list_by_n(l, n):
        # Groups the given list into sub list groups of 'n'.
        grouped_list = [l[i:i + n] for i in range(0, len(l), n)]
        return grouped_list

    @staticmethod
    def convert_CamelCase_to_underscore(s):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @staticmethod
    def convert_underscore_to_CamelCase(s):
        s = s.lower()
        return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)
