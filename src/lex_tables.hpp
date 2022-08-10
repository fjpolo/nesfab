#include <cstdint>
#include <string_view>
using token_type_t = std::uint32_t;
constexpr token_type_t TOK_ERROR = 0;
constexpr token_type_t TOK_eof = 1;
constexpr token_type_t TOK_comment = 2;
constexpr token_type_t TOK_eol = 3;
constexpr token_type_t TOK_whitespace = 4;
constexpr token_type_t TOK_if = 5;
constexpr token_type_t TOK_else = 6;
constexpr token_type_t TOK_for = 7;
constexpr token_type_t TOK_while = 8;
constexpr token_type_t TOK_do = 9;
constexpr token_type_t TOK_break = 10;
constexpr token_type_t TOK_continue = 11;
constexpr token_type_t TOK_return = 12;
constexpr token_type_t TOK_fn = 13;
constexpr token_type_t TOK_ct = 14;
constexpr token_type_t TOK_mode = 15;
constexpr token_type_t TOK_nmi = 16;
constexpr token_type_t TOK_goto = 17;
constexpr token_type_t TOK_label = 18;
constexpr token_type_t TOK_using = 19;
constexpr token_type_t TOK_file = 20;
constexpr token_type_t TOK_struct = 21;
constexpr token_type_t TOK_vars = 22;
constexpr token_type_t TOK_data = 23;
constexpr token_type_t TOK_omni = 24;
constexpr token_type_t TOK_ready = 25;
constexpr token_type_t TOK_fence = 26;
constexpr token_type_t TOK_PPUCTRL = 27;
constexpr token_type_t TOK_PPUMASK = 28;
constexpr token_type_t TOK_PPUSTATUS = 29;
constexpr token_type_t TOK_PPUSCROLL = 30;
constexpr token_type_t TOK_PPUADDR = 31;
constexpr token_type_t TOK_PPUDATA = 32;
constexpr token_type_t TOK_OAMADDR = 33;
constexpr token_type_t TOK_OAMDATA = 34;
constexpr token_type_t TOK_OAMDMA = 35;
constexpr token_type_t TOK_lbrace = 36;
constexpr token_type_t TOK_rbrace = 37;
constexpr token_type_t TOK_lbracket = 38;
constexpr token_type_t TOK_rbracket = 39;
constexpr token_type_t TOK_colon = 40;
constexpr token_type_t TOK_dquote = 41;
constexpr token_type_t TOK_quote = 42;
constexpr token_type_t TOK_semicolon = 43;
constexpr token_type_t TOK_comma = 44;
constexpr token_type_t TOK_lparen = 45;
constexpr token_type_t TOK_at = 46;
constexpr token_type_t TOK_period = 47;
constexpr token_type_t TOK_sizeof = 48;
constexpr token_type_t TOK_sizeof_expr = 49;
constexpr token_type_t TOK_len = 50;
constexpr token_type_t TOK_len_expr = 51;
constexpr token_type_t TOK_apply = 52;
constexpr token_type_t TOK_cast_argn = 53;
constexpr token_type_t TOK_cast_type = 54;
constexpr token_type_t TOK_index = 55;
constexpr token_type_t TOK_unary_minus = 56;
constexpr token_type_t TOK_unary_xor = 57;
constexpr token_type_t TOK_unary_negate = 58;
constexpr token_type_t TOK_asterisk = 59;
constexpr token_type_t TOK_fslash = 60;
constexpr token_type_t TOK_plus = 61;
constexpr token_type_t TOK_minus = 62;
constexpr token_type_t TOK_lshift = 63;
constexpr token_type_t TOK_rshift = 64;
constexpr token_type_t TOK_bitwise_and = 65;
constexpr token_type_t TOK_bitwise_xor = 66;
constexpr token_type_t TOK_bitwise_or = 67;
constexpr token_type_t TOK_lt = 68;
constexpr token_type_t TOK_lte = 69;
constexpr token_type_t TOK_gt = 70;
constexpr token_type_t TOK_gte = 71;
constexpr token_type_t TOK_eq = 72;
constexpr token_type_t TOK_not_eq = 73;
constexpr token_type_t TOK_logical_and = 74;
constexpr token_type_t TOK_end_logical_and = 75;
constexpr token_type_t TOK_logical_or = 76;
constexpr token_type_t TOK_end_logical_or = 77;
constexpr token_type_t TOK_assign = 78;
constexpr token_type_t TOK_plus_assign = 79;
constexpr token_type_t TOK_minus_assign = 80;
constexpr token_type_t TOK_times_assign = 81;
constexpr token_type_t TOK_div_assign = 82;
constexpr token_type_t TOK_bitwise_and_assign = 83;
constexpr token_type_t TOK_logical_and_assign = 84;
constexpr token_type_t TOK_bitwise_or_assign = 85;
constexpr token_type_t TOK_logical_or_assign = 86;
constexpr token_type_t TOK_bitwise_xor_assign = 87;
constexpr token_type_t TOK_lshift_assign = 88;
constexpr token_type_t TOK_rshift_assign = 89;
constexpr token_type_t TOK_rparen = 90;
constexpr token_type_t TOK_Void = 91;
constexpr token_type_t TOK_F = 92;
constexpr token_type_t TOK_FF = 93;
constexpr token_type_t TOK_FFF = 94;
constexpr token_type_t TOK_U = 95;
constexpr token_type_t TOK_UU = 96;
constexpr token_type_t TOK_UUU = 97;
constexpr token_type_t TOK_UF = 98;
constexpr token_type_t TOK_UUF = 99;
constexpr token_type_t TOK_UUUF = 100;
constexpr token_type_t TOK_UFF = 101;
constexpr token_type_t TOK_UUFF = 102;
constexpr token_type_t TOK_UUUFF = 103;
constexpr token_type_t TOK_UFFF = 104;
constexpr token_type_t TOK_UUFFF = 105;
constexpr token_type_t TOK_UUUFFF = 106;
constexpr token_type_t TOK_S = 107;
constexpr token_type_t TOK_SS = 108;
constexpr token_type_t TOK_SSS = 109;
constexpr token_type_t TOK_SF = 110;
constexpr token_type_t TOK_SSF = 111;
constexpr token_type_t TOK_SSSF = 112;
constexpr token_type_t TOK_SFF = 113;
constexpr token_type_t TOK_SSFF = 114;
constexpr token_type_t TOK_SSSFF = 115;
constexpr token_type_t TOK_SFFF = 116;
constexpr token_type_t TOK_SSFFF = 117;
constexpr token_type_t TOK_SSSFFF = 118;
constexpr token_type_t TOK_PP = 119;
constexpr token_type_t TOK_PPP = 120;
constexpr token_type_t TOK_MM = 121;
constexpr token_type_t TOK_MMM = 122;
constexpr token_type_t TOK_Int = 123;
constexpr token_type_t TOK_Real = 124;
constexpr token_type_t TOK_Bool = 125;
constexpr token_type_t TOK_ident = 126;
constexpr token_type_t TOK_type_ident = 127;
constexpr token_type_t TOK_decimal = 128;
constexpr token_type_t TOK_hex = 129;
constexpr token_type_t TOK_binary = 130;
constexpr token_type_t TOK_int = 131;
constexpr token_type_t TOK_real = 132;
constexpr token_type_t TOK_global_ident = 133;
constexpr token_type_t TOK_weak_ident = 134;
constexpr token_type_t TOK_hw_expr = 135;
constexpr token_type_t TOK_hw_addr = 136;
constexpr token_type_t TOK_read_hw = 137;
constexpr token_type_t TOK_write_hw = 138;
constexpr token_type_t TOK_push_paa_byte_array = 139;
constexpr token_type_t TOK_push_paa = 140;
constexpr token_type_t TOK_begin_paa = 141;
constexpr token_type_t TOK_end_paa = 142;
constexpr token_type_t TOK_group_set = 143;
constexpr token_type_t TOK_spair = 144;
constexpr token_type_t TOK_END = 145;
inline std::string_view token_name(token_type_t type)
{
    using namespace std::literals;
    switch(type)
    {
    default: return "?BAD?"sv;
    case TOK_eof: return "eof"sv;
    case TOK_comment: return "comment"sv;
    case TOK_eol: return "eol"sv;
    case TOK_whitespace: return "whitespace"sv;
    case TOK_if: return "if"sv;
    case TOK_else: return "else"sv;
    case TOK_for: return "for"sv;
    case TOK_while: return "while"sv;
    case TOK_do: return "do"sv;
    case TOK_break: return "break"sv;
    case TOK_continue: return "continue"sv;
    case TOK_return: return "return"sv;
    case TOK_fn: return "fn"sv;
    case TOK_ct: return "ct"sv;
    case TOK_mode: return "mode"sv;
    case TOK_nmi: return "nmi"sv;
    case TOK_goto: return "goto"sv;
    case TOK_label: return "label"sv;
    case TOK_using: return "using"sv;
    case TOK_file: return "file"sv;
    case TOK_struct: return "struct"sv;
    case TOK_vars: return "vars"sv;
    case TOK_data: return "data"sv;
    case TOK_omni: return "omni"sv;
    case TOK_ready: return "ready"sv;
    case TOK_fence: return "fence"sv;
    case TOK_PPUCTRL: return "PPUCTRL"sv;
    case TOK_PPUMASK: return "PPUMASK"sv;
    case TOK_PPUSTATUS: return "PPUSTATUS"sv;
    case TOK_PPUSCROLL: return "PPUSCROLL"sv;
    case TOK_PPUADDR: return "PPUADDR"sv;
    case TOK_PPUDATA: return "PPUDATA"sv;
    case TOK_OAMADDR: return "OAMADDR"sv;
    case TOK_OAMDATA: return "OAMDATA"sv;
    case TOK_OAMDMA: return "OAMDMA"sv;
    case TOK_lbrace: return "lbrace"sv;
    case TOK_rbrace: return "rbrace"sv;
    case TOK_lbracket: return "lbracket"sv;
    case TOK_rbracket: return "rbracket"sv;
    case TOK_colon: return "colon"sv;
    case TOK_dquote: return "dquote"sv;
    case TOK_quote: return "quote"sv;
    case TOK_semicolon: return "semicolon"sv;
    case TOK_comma: return "comma"sv;
    case TOK_lparen: return "lparen"sv;
    case TOK_at: return "at"sv;
    case TOK_period: return "period"sv;
    case TOK_sizeof: return "sizeof"sv;
    case TOK_sizeof_expr: return "sizeof_expr"sv;
    case TOK_len: return "len"sv;
    case TOK_len_expr: return "len_expr"sv;
    case TOK_apply: return "apply"sv;
    case TOK_cast_argn: return "cast_argn"sv;
    case TOK_cast_type: return "cast_type"sv;
    case TOK_index: return "index"sv;
    case TOK_unary_minus: return "unary_minus"sv;
    case TOK_unary_xor: return "unary_xor"sv;
    case TOK_unary_negate: return "unary_negate"sv;
    case TOK_asterisk: return "asterisk"sv;
    case TOK_fslash: return "fslash"sv;
    case TOK_plus: return "plus"sv;
    case TOK_minus: return "minus"sv;
    case TOK_lshift: return "lshift"sv;
    case TOK_rshift: return "rshift"sv;
    case TOK_bitwise_and: return "bitwise_and"sv;
    case TOK_bitwise_xor: return "bitwise_xor"sv;
    case TOK_bitwise_or: return "bitwise_or"sv;
    case TOK_lt: return "lt"sv;
    case TOK_lte: return "lte"sv;
    case TOK_gt: return "gt"sv;
    case TOK_gte: return "gte"sv;
    case TOK_eq: return "eq"sv;
    case TOK_not_eq: return "not_eq"sv;
    case TOK_logical_and: return "logical_and"sv;
    case TOK_end_logical_and: return "end_logical_and"sv;
    case TOK_logical_or: return "logical_or"sv;
    case TOK_end_logical_or: return "end_logical_or"sv;
    case TOK_assign: return "assign"sv;
    case TOK_plus_assign: return "plus_assign"sv;
    case TOK_minus_assign: return "minus_assign"sv;
    case TOK_times_assign: return "times_assign"sv;
    case TOK_div_assign: return "div_assign"sv;
    case TOK_bitwise_and_assign: return "bitwise_and_assign"sv;
    case TOK_logical_and_assign: return "logical_and_assign"sv;
    case TOK_bitwise_or_assign: return "bitwise_or_assign"sv;
    case TOK_logical_or_assign: return "logical_or_assign"sv;
    case TOK_bitwise_xor_assign: return "bitwise_xor_assign"sv;
    case TOK_lshift_assign: return "lshift_assign"sv;
    case TOK_rshift_assign: return "rshift_assign"sv;
    case TOK_rparen: return "rparen"sv;
    case TOK_Void: return "Void"sv;
    case TOK_F: return "F"sv;
    case TOK_FF: return "FF"sv;
    case TOK_FFF: return "FFF"sv;
    case TOK_U: return "U"sv;
    case TOK_UU: return "UU"sv;
    case TOK_UUU: return "UUU"sv;
    case TOK_UF: return "UF"sv;
    case TOK_UUF: return "UUF"sv;
    case TOK_UUUF: return "UUUF"sv;
    case TOK_UFF: return "UFF"sv;
    case TOK_UUFF: return "UUFF"sv;
    case TOK_UUUFF: return "UUUFF"sv;
    case TOK_UFFF: return "UFFF"sv;
    case TOK_UUFFF: return "UUFFF"sv;
    case TOK_UUUFFF: return "UUUFFF"sv;
    case TOK_S: return "S"sv;
    case TOK_SS: return "SS"sv;
    case TOK_SSS: return "SSS"sv;
    case TOK_SF: return "SF"sv;
    case TOK_SSF: return "SSF"sv;
    case TOK_SSSF: return "SSSF"sv;
    case TOK_SFF: return "SFF"sv;
    case TOK_SSFF: return "SSFF"sv;
    case TOK_SSSFF: return "SSSFF"sv;
    case TOK_SFFF: return "SFFF"sv;
    case TOK_SSFFF: return "SSFFF"sv;
    case TOK_SSSFFF: return "SSSFFF"sv;
    case TOK_PP: return "PP"sv;
    case TOK_PPP: return "PPP"sv;
    case TOK_MM: return "MM"sv;
    case TOK_MMM: return "MMM"sv;
    case TOK_Int: return "Int"sv;
    case TOK_Real: return "Real"sv;
    case TOK_Bool: return "Bool"sv;
    case TOK_ident: return "ident"sv;
    case TOK_type_ident: return "type_ident"sv;
    case TOK_decimal: return "decimal"sv;
    case TOK_hex: return "hex"sv;
    case TOK_binary: return "binary"sv;
    case TOK_int: return "int"sv;
    case TOK_real: return "real"sv;
    case TOK_global_ident: return "global_ident"sv;
    case TOK_weak_ident: return "weak_ident"sv;
    case TOK_hw_expr: return "hw_expr"sv;
    case TOK_hw_addr: return "hw_addr"sv;
    case TOK_read_hw: return "read_hw"sv;
    case TOK_write_hw: return "write_hw"sv;
    case TOK_push_paa_byte_array: return "push_paa_byte_array"sv;
    case TOK_push_paa: return "push_paa"sv;
    case TOK_begin_paa: return "begin_paa"sv;
    case TOK_end_paa: return "end_paa"sv;
    case TOK_group_set: return "group_set"sv;
    case TOK_spair: return "spair"sv;
    }
}
inline std::string_view token_string(token_type_t type)
{
    using namespace std::literals;
    switch(type)
    {
    default: return "?BAD?"sv;
    case TOK_eof: return "file ending"sv;
    case TOK_comment: return "comment"sv;
    case TOK_eol: return "line ending"sv;
    case TOK_whitespace: return "space"sv;
    case TOK_if: return "if"sv;
    case TOK_else: return "else"sv;
    case TOK_for: return "for"sv;
    case TOK_while: return "while"sv;
    case TOK_do: return "do"sv;
    case TOK_break: return "break"sv;
    case TOK_continue: return "continue"sv;
    case TOK_return: return "return"sv;
    case TOK_fn: return "fn"sv;
    case TOK_ct: return "ct"sv;
    case TOK_mode: return "mode"sv;
    case TOK_nmi: return "nmi"sv;
    case TOK_goto: return "goto"sv;
    case TOK_label: return "label"sv;
    case TOK_using: return "using"sv;
    case TOK_file: return "file"sv;
    case TOK_struct: return "struct"sv;
    case TOK_vars: return "vars"sv;
    case TOK_data: return "data"sv;
    case TOK_omni: return "omni"sv;
    case TOK_ready: return "ready"sv;
    case TOK_fence: return "fence"sv;
    case TOK_PPUCTRL: return "PPUCTRL"sv;
    case TOK_PPUMASK: return "PPUMASK"sv;
    case TOK_PPUSTATUS: return "PPUSTATUS"sv;
    case TOK_PPUSCROLL: return "PPUSCROLL"sv;
    case TOK_PPUADDR: return "PPUADDR"sv;
    case TOK_PPUDATA: return "PPUDATA"sv;
    case TOK_OAMADDR: return "OAMADDR"sv;
    case TOK_OAMDATA: return "OAMDATA"sv;
    case TOK_OAMDMA: return "OAMDMA"sv;
    case TOK_lbrace: return "lbrace"sv;
    case TOK_rbrace: return "rbrace"sv;
    case TOK_lbracket: return "lbracket"sv;
    case TOK_rbracket: return "rbracket"sv;
    case TOK_colon: return "colon"sv;
    case TOK_dquote: return "dquote"sv;
    case TOK_quote: return "quote"sv;
    case TOK_semicolon: return "semicolon"sv;
    case TOK_comma: return "comma"sv;
    case TOK_lparen: return "lparen"sv;
    case TOK_at: return "at"sv;
    case TOK_period: return "period"sv;
    case TOK_sizeof: return "sizeof"sv;
    case TOK_sizeof_expr: return "sizeof"sv;
    case TOK_len: return "len"sv;
    case TOK_len_expr: return "len"sv;
    case TOK_apply: return "apply"sv;
    case TOK_cast_argn: return "cast"sv;
    case TOK_cast_type: return "cast type"sv;
    case TOK_index: return "index"sv;
    case TOK_unary_minus: return "unary -"sv;
    case TOK_unary_xor: return "~"sv;
    case TOK_unary_negate: return "!"sv;
    case TOK_asterisk: return "*"sv;
    case TOK_fslash: return "/"sv;
    case TOK_plus: return "+"sv;
    case TOK_minus: return "-"sv;
    case TOK_lshift: return "<<"sv;
    case TOK_rshift: return ">>"sv;
    case TOK_bitwise_and: return "&"sv;
    case TOK_bitwise_xor: return "^"sv;
    case TOK_bitwise_or: return "|"sv;
    case TOK_lt: return "<"sv;
    case TOK_lte: return "<="sv;
    case TOK_gt: return ">"sv;
    case TOK_gte: return ">="sv;
    case TOK_eq: return "=="sv;
    case TOK_not_eq: return "!="sv;
    case TOK_logical_and: return "&&"sv;
    case TOK_end_logical_and: return "end_logical_and"sv;
    case TOK_logical_or: return "||"sv;
    case TOK_end_logical_or: return "end_logical_or"sv;
    case TOK_assign: return "="sv;
    case TOK_plus_assign: return "+="sv;
    case TOK_minus_assign: return "-="sv;
    case TOK_times_assign: return "*="sv;
    case TOK_div_assign: return "/="sv;
    case TOK_bitwise_and_assign: return "&="sv;
    case TOK_logical_and_assign: return "&&="sv;
    case TOK_bitwise_or_assign: return "|="sv;
    case TOK_logical_or_assign: return "||="sv;
    case TOK_bitwise_xor_assign: return "^="sv;
    case TOK_lshift_assign: return "<<="sv;
    case TOK_rshift_assign: return ">>="sv;
    case TOK_rparen: return "rparen"sv;
    case TOK_Void: return "void type"sv;
    case TOK_F: return "F type"sv;
    case TOK_FF: return "FF type"sv;
    case TOK_FFF: return "FFF type"sv;
    case TOK_U: return "U type"sv;
    case TOK_UU: return "UU type"sv;
    case TOK_UUU: return "UUU type"sv;
    case TOK_UF: return "UF type"sv;
    case TOK_UUF: return "UUF type"sv;
    case TOK_UUUF: return "UUUF type"sv;
    case TOK_UFF: return "UFF type"sv;
    case TOK_UUFF: return "UUFF type"sv;
    case TOK_UUUFF: return "UUUFF type"sv;
    case TOK_UFFF: return "UFFF type"sv;
    case TOK_UUFFF: return "UUFFF type"sv;
    case TOK_UUUFFF: return "UUUFFF type"sv;
    case TOK_S: return "S type"sv;
    case TOK_SS: return "SS type"sv;
    case TOK_SSS: return "SSS type"sv;
    case TOK_SF: return "SF type"sv;
    case TOK_SSF: return "SSF type"sv;
    case TOK_SSSF: return "SSSF type"sv;
    case TOK_SFF: return "SFF type"sv;
    case TOK_SSFF: return "SSFF type"sv;
    case TOK_SSSFF: return "SSSFF type"sv;
    case TOK_SFFF: return "SFFF type"sv;
    case TOK_SSFFF: return "SSFFF type"sv;
    case TOK_SSSFFF: return "SSSFFF type"sv;
    case TOK_PP: return "PP type"sv;
    case TOK_PPP: return "PPP type"sv;
    case TOK_MM: return "MM type"sv;
    case TOK_MMM: return "MMM type"sv;
    case TOK_Int: return "Int type"sv;
    case TOK_Real: return "Real type"sv;
    case TOK_Bool: return "Bool type"sv;
    case TOK_ident: return "identifier"sv;
    case TOK_type_ident: return "type identifier"sv;
    case TOK_decimal: return "number"sv;
    case TOK_hex: return "number"sv;
    case TOK_binary: return "number"sv;
    case TOK_int: return "int"sv;
    case TOK_real: return "real"sv;
    case TOK_global_ident: return "global identifier"sv;
    case TOK_weak_ident: return "weak identifier"sv;
    case TOK_hw_expr: return "hardware expression"sv;
    case TOK_hw_addr: return "hardware address"sv;
    case TOK_read_hw: return "read hardware"sv;
    case TOK_write_hw: return "write hardware"sv;
    case TOK_push_paa_byte_array: return "byte array"sv;
    case TOK_push_paa: return "push paa"sv;
    case TOK_begin_paa: return "begin paa"sv;
    case TOK_end_paa: return "end paa"sv;
    case TOK_group_set: return "group set"sv;
    case TOK_spair: return "spair"sv;
    }
}
constexpr unsigned char token_precedence_table[] =
{
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    6,
    6,
    1,
    4,
    5,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    8,
    8,
    8,
    10,
    10,
    11,
    11,
    12,
    12,
    13,
    14,
    15,
    16,
    16,
    16,
    16,
    17,
    17,
    18,
    18,
    19,
    19,
    158,
    158,
    158,
    158,
    158,
    158,
    158,
    158,
    158,
    158,
    158,
    158,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
};
constexpr bool token_right_assoc_table[] =
{
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
};
#define TOK_KEY_CASES \
    case TOK_if:\
    case TOK_else:\
    case TOK_for:\
    case TOK_while:\
    case TOK_do:\
    case TOK_break:\
    case TOK_continue:\
    case TOK_return:\
    case TOK_fn:\
    case TOK_ct:\
    case TOK_mode:\
    case TOK_nmi:\
    case TOK_goto:\
    case TOK_label:\
    case TOK_using:\
    case TOK_file:\
    case TOK_struct:\
    case TOK_vars:\
    case TOK_data:\
    case TOK_omni:\
    case TOK_ready:\
    case TOK_fence:\
    case TOK_PPUCTRL:\
    case TOK_PPUMASK:\
    case TOK_PPUSTATUS:\
    case TOK_PPUSCROLL:\
    case TOK_PPUADDR:\
    case TOK_PPUDATA:\
    case TOK_OAMADDR:\
    case TOK_OAMDATA:\
    case TOK_OAMDMA:\
    case TOK_lbrace:\
    case TOK_rbrace:\
    case TOK_lbracket:\
    case TOK_rbracket:\
    case TOK_colon:\
    case TOK_dquote:\
    case TOK_quote:\
    case TOK_semicolon:\
    case TOK_comma:\
    case TOK_lparen:\
    case TOK_at:\
    case TOK_period:\
    case TOK_sizeof:\
    case TOK_sizeof_expr:\
    case TOK_len:\
    case TOK_len_expr:\
    case TOK_apply:\
    case TOK_cast_argn:\
    case TOK_cast_type:\
    case TOK_index:\
    case TOK_unary_minus:\
    case TOK_unary_xor:\
    case TOK_unary_negate:\
    case TOK_asterisk:\
    case TOK_fslash:\
    case TOK_plus:\
    case TOK_minus:\
    case TOK_lshift:\
    case TOK_rshift:\
    case TOK_bitwise_and:\
    case TOK_bitwise_xor:\
    case TOK_bitwise_or:\
    case TOK_lt:\
    case TOK_lte:\
    case TOK_gt:\
    case TOK_gte:\
    case TOK_eq:\
    case TOK_not_eq:\
    case TOK_logical_and:\
    case TOK_end_logical_and:\
    case TOK_logical_or:\
    case TOK_end_logical_or:\
    case TOK_assign:\
    case TOK_plus_assign:\
    case TOK_minus_assign:\
    case TOK_times_assign:\
    case TOK_div_assign:\
    case TOK_bitwise_and_assign:\
    case TOK_logical_and_assign:\
    case TOK_bitwise_or_assign:\
    case TOK_logical_or_assign:\
    case TOK_bitwise_xor_assign:\
    case TOK_lshift_assign:\
    case TOK_rshift_assign:\
    case TOK_rparen:\

constexpr token_type_t TOK_LAST_STATE = 144;
constexpr token_type_t TOK_START = 145;
extern unsigned const lexer_ec_table[256];
extern token_type_t const lexer_transition_table[30261];
