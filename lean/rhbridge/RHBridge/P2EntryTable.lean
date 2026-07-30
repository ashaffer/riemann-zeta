/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2EntryCertificate

/-!
# Explicit 600-entry table for the canonical `p = 2` certificate

This generated row-major table identifies `Fin 600` with the two
upper-triangular `24 × 24` parity blocks.  It gives later generated
analytic certificates a stable, concrete index order.  Lean verifies a
left inverse and then uses the already proved cardinality to establish
bijectivity; no external enumeration claim is trusted.
-/

namespace RHP2Bridge

noncomputable section

/-- Generated row-major enumeration: even entries first, then odd entries. -/
def p2UpperEntryAtNat : ℕ → P2UpperEntryIndex
  | 0 => ⟨⟨.even, 0, 0⟩, by decide⟩
  | 1 => ⟨⟨.even, 0, 1⟩, by decide⟩
  | 2 => ⟨⟨.even, 0, 2⟩, by decide⟩
  | 3 => ⟨⟨.even, 0, 3⟩, by decide⟩
  | 4 => ⟨⟨.even, 0, 4⟩, by decide⟩
  | 5 => ⟨⟨.even, 0, 5⟩, by decide⟩
  | 6 => ⟨⟨.even, 0, 6⟩, by decide⟩
  | 7 => ⟨⟨.even, 0, 7⟩, by decide⟩
  | 8 => ⟨⟨.even, 0, 8⟩, by decide⟩
  | 9 => ⟨⟨.even, 0, 9⟩, by decide⟩
  | 10 => ⟨⟨.even, 0, 10⟩, by decide⟩
  | 11 => ⟨⟨.even, 0, 11⟩, by decide⟩
  | 12 => ⟨⟨.even, 0, 12⟩, by decide⟩
  | 13 => ⟨⟨.even, 0, 13⟩, by decide⟩
  | 14 => ⟨⟨.even, 0, 14⟩, by decide⟩
  | 15 => ⟨⟨.even, 0, 15⟩, by decide⟩
  | 16 => ⟨⟨.even, 0, 16⟩, by decide⟩
  | 17 => ⟨⟨.even, 0, 17⟩, by decide⟩
  | 18 => ⟨⟨.even, 0, 18⟩, by decide⟩
  | 19 => ⟨⟨.even, 0, 19⟩, by decide⟩
  | 20 => ⟨⟨.even, 0, 20⟩, by decide⟩
  | 21 => ⟨⟨.even, 0, 21⟩, by decide⟩
  | 22 => ⟨⟨.even, 0, 22⟩, by decide⟩
  | 23 => ⟨⟨.even, 0, 23⟩, by decide⟩
  | 24 => ⟨⟨.even, 1, 1⟩, by decide⟩
  | 25 => ⟨⟨.even, 1, 2⟩, by decide⟩
  | 26 => ⟨⟨.even, 1, 3⟩, by decide⟩
  | 27 => ⟨⟨.even, 1, 4⟩, by decide⟩
  | 28 => ⟨⟨.even, 1, 5⟩, by decide⟩
  | 29 => ⟨⟨.even, 1, 6⟩, by decide⟩
  | 30 => ⟨⟨.even, 1, 7⟩, by decide⟩
  | 31 => ⟨⟨.even, 1, 8⟩, by decide⟩
  | 32 => ⟨⟨.even, 1, 9⟩, by decide⟩
  | 33 => ⟨⟨.even, 1, 10⟩, by decide⟩
  | 34 => ⟨⟨.even, 1, 11⟩, by decide⟩
  | 35 => ⟨⟨.even, 1, 12⟩, by decide⟩
  | 36 => ⟨⟨.even, 1, 13⟩, by decide⟩
  | 37 => ⟨⟨.even, 1, 14⟩, by decide⟩
  | 38 => ⟨⟨.even, 1, 15⟩, by decide⟩
  | 39 => ⟨⟨.even, 1, 16⟩, by decide⟩
  | 40 => ⟨⟨.even, 1, 17⟩, by decide⟩
  | 41 => ⟨⟨.even, 1, 18⟩, by decide⟩
  | 42 => ⟨⟨.even, 1, 19⟩, by decide⟩
  | 43 => ⟨⟨.even, 1, 20⟩, by decide⟩
  | 44 => ⟨⟨.even, 1, 21⟩, by decide⟩
  | 45 => ⟨⟨.even, 1, 22⟩, by decide⟩
  | 46 => ⟨⟨.even, 1, 23⟩, by decide⟩
  | 47 => ⟨⟨.even, 2, 2⟩, by decide⟩
  | 48 => ⟨⟨.even, 2, 3⟩, by decide⟩
  | 49 => ⟨⟨.even, 2, 4⟩, by decide⟩
  | 50 => ⟨⟨.even, 2, 5⟩, by decide⟩
  | 51 => ⟨⟨.even, 2, 6⟩, by decide⟩
  | 52 => ⟨⟨.even, 2, 7⟩, by decide⟩
  | 53 => ⟨⟨.even, 2, 8⟩, by decide⟩
  | 54 => ⟨⟨.even, 2, 9⟩, by decide⟩
  | 55 => ⟨⟨.even, 2, 10⟩, by decide⟩
  | 56 => ⟨⟨.even, 2, 11⟩, by decide⟩
  | 57 => ⟨⟨.even, 2, 12⟩, by decide⟩
  | 58 => ⟨⟨.even, 2, 13⟩, by decide⟩
  | 59 => ⟨⟨.even, 2, 14⟩, by decide⟩
  | 60 => ⟨⟨.even, 2, 15⟩, by decide⟩
  | 61 => ⟨⟨.even, 2, 16⟩, by decide⟩
  | 62 => ⟨⟨.even, 2, 17⟩, by decide⟩
  | 63 => ⟨⟨.even, 2, 18⟩, by decide⟩
  | 64 => ⟨⟨.even, 2, 19⟩, by decide⟩
  | 65 => ⟨⟨.even, 2, 20⟩, by decide⟩
  | 66 => ⟨⟨.even, 2, 21⟩, by decide⟩
  | 67 => ⟨⟨.even, 2, 22⟩, by decide⟩
  | 68 => ⟨⟨.even, 2, 23⟩, by decide⟩
  | 69 => ⟨⟨.even, 3, 3⟩, by decide⟩
  | 70 => ⟨⟨.even, 3, 4⟩, by decide⟩
  | 71 => ⟨⟨.even, 3, 5⟩, by decide⟩
  | 72 => ⟨⟨.even, 3, 6⟩, by decide⟩
  | 73 => ⟨⟨.even, 3, 7⟩, by decide⟩
  | 74 => ⟨⟨.even, 3, 8⟩, by decide⟩
  | 75 => ⟨⟨.even, 3, 9⟩, by decide⟩
  | 76 => ⟨⟨.even, 3, 10⟩, by decide⟩
  | 77 => ⟨⟨.even, 3, 11⟩, by decide⟩
  | 78 => ⟨⟨.even, 3, 12⟩, by decide⟩
  | 79 => ⟨⟨.even, 3, 13⟩, by decide⟩
  | 80 => ⟨⟨.even, 3, 14⟩, by decide⟩
  | 81 => ⟨⟨.even, 3, 15⟩, by decide⟩
  | 82 => ⟨⟨.even, 3, 16⟩, by decide⟩
  | 83 => ⟨⟨.even, 3, 17⟩, by decide⟩
  | 84 => ⟨⟨.even, 3, 18⟩, by decide⟩
  | 85 => ⟨⟨.even, 3, 19⟩, by decide⟩
  | 86 => ⟨⟨.even, 3, 20⟩, by decide⟩
  | 87 => ⟨⟨.even, 3, 21⟩, by decide⟩
  | 88 => ⟨⟨.even, 3, 22⟩, by decide⟩
  | 89 => ⟨⟨.even, 3, 23⟩, by decide⟩
  | 90 => ⟨⟨.even, 4, 4⟩, by decide⟩
  | 91 => ⟨⟨.even, 4, 5⟩, by decide⟩
  | 92 => ⟨⟨.even, 4, 6⟩, by decide⟩
  | 93 => ⟨⟨.even, 4, 7⟩, by decide⟩
  | 94 => ⟨⟨.even, 4, 8⟩, by decide⟩
  | 95 => ⟨⟨.even, 4, 9⟩, by decide⟩
  | 96 => ⟨⟨.even, 4, 10⟩, by decide⟩
  | 97 => ⟨⟨.even, 4, 11⟩, by decide⟩
  | 98 => ⟨⟨.even, 4, 12⟩, by decide⟩
  | 99 => ⟨⟨.even, 4, 13⟩, by decide⟩
  | 100 => ⟨⟨.even, 4, 14⟩, by decide⟩
  | 101 => ⟨⟨.even, 4, 15⟩, by decide⟩
  | 102 => ⟨⟨.even, 4, 16⟩, by decide⟩
  | 103 => ⟨⟨.even, 4, 17⟩, by decide⟩
  | 104 => ⟨⟨.even, 4, 18⟩, by decide⟩
  | 105 => ⟨⟨.even, 4, 19⟩, by decide⟩
  | 106 => ⟨⟨.even, 4, 20⟩, by decide⟩
  | 107 => ⟨⟨.even, 4, 21⟩, by decide⟩
  | 108 => ⟨⟨.even, 4, 22⟩, by decide⟩
  | 109 => ⟨⟨.even, 4, 23⟩, by decide⟩
  | 110 => ⟨⟨.even, 5, 5⟩, by decide⟩
  | 111 => ⟨⟨.even, 5, 6⟩, by decide⟩
  | 112 => ⟨⟨.even, 5, 7⟩, by decide⟩
  | 113 => ⟨⟨.even, 5, 8⟩, by decide⟩
  | 114 => ⟨⟨.even, 5, 9⟩, by decide⟩
  | 115 => ⟨⟨.even, 5, 10⟩, by decide⟩
  | 116 => ⟨⟨.even, 5, 11⟩, by decide⟩
  | 117 => ⟨⟨.even, 5, 12⟩, by decide⟩
  | 118 => ⟨⟨.even, 5, 13⟩, by decide⟩
  | 119 => ⟨⟨.even, 5, 14⟩, by decide⟩
  | 120 => ⟨⟨.even, 5, 15⟩, by decide⟩
  | 121 => ⟨⟨.even, 5, 16⟩, by decide⟩
  | 122 => ⟨⟨.even, 5, 17⟩, by decide⟩
  | 123 => ⟨⟨.even, 5, 18⟩, by decide⟩
  | 124 => ⟨⟨.even, 5, 19⟩, by decide⟩
  | 125 => ⟨⟨.even, 5, 20⟩, by decide⟩
  | 126 => ⟨⟨.even, 5, 21⟩, by decide⟩
  | 127 => ⟨⟨.even, 5, 22⟩, by decide⟩
  | 128 => ⟨⟨.even, 5, 23⟩, by decide⟩
  | 129 => ⟨⟨.even, 6, 6⟩, by decide⟩
  | 130 => ⟨⟨.even, 6, 7⟩, by decide⟩
  | 131 => ⟨⟨.even, 6, 8⟩, by decide⟩
  | 132 => ⟨⟨.even, 6, 9⟩, by decide⟩
  | 133 => ⟨⟨.even, 6, 10⟩, by decide⟩
  | 134 => ⟨⟨.even, 6, 11⟩, by decide⟩
  | 135 => ⟨⟨.even, 6, 12⟩, by decide⟩
  | 136 => ⟨⟨.even, 6, 13⟩, by decide⟩
  | 137 => ⟨⟨.even, 6, 14⟩, by decide⟩
  | 138 => ⟨⟨.even, 6, 15⟩, by decide⟩
  | 139 => ⟨⟨.even, 6, 16⟩, by decide⟩
  | 140 => ⟨⟨.even, 6, 17⟩, by decide⟩
  | 141 => ⟨⟨.even, 6, 18⟩, by decide⟩
  | 142 => ⟨⟨.even, 6, 19⟩, by decide⟩
  | 143 => ⟨⟨.even, 6, 20⟩, by decide⟩
  | 144 => ⟨⟨.even, 6, 21⟩, by decide⟩
  | 145 => ⟨⟨.even, 6, 22⟩, by decide⟩
  | 146 => ⟨⟨.even, 6, 23⟩, by decide⟩
  | 147 => ⟨⟨.even, 7, 7⟩, by decide⟩
  | 148 => ⟨⟨.even, 7, 8⟩, by decide⟩
  | 149 => ⟨⟨.even, 7, 9⟩, by decide⟩
  | 150 => ⟨⟨.even, 7, 10⟩, by decide⟩
  | 151 => ⟨⟨.even, 7, 11⟩, by decide⟩
  | 152 => ⟨⟨.even, 7, 12⟩, by decide⟩
  | 153 => ⟨⟨.even, 7, 13⟩, by decide⟩
  | 154 => ⟨⟨.even, 7, 14⟩, by decide⟩
  | 155 => ⟨⟨.even, 7, 15⟩, by decide⟩
  | 156 => ⟨⟨.even, 7, 16⟩, by decide⟩
  | 157 => ⟨⟨.even, 7, 17⟩, by decide⟩
  | 158 => ⟨⟨.even, 7, 18⟩, by decide⟩
  | 159 => ⟨⟨.even, 7, 19⟩, by decide⟩
  | 160 => ⟨⟨.even, 7, 20⟩, by decide⟩
  | 161 => ⟨⟨.even, 7, 21⟩, by decide⟩
  | 162 => ⟨⟨.even, 7, 22⟩, by decide⟩
  | 163 => ⟨⟨.even, 7, 23⟩, by decide⟩
  | 164 => ⟨⟨.even, 8, 8⟩, by decide⟩
  | 165 => ⟨⟨.even, 8, 9⟩, by decide⟩
  | 166 => ⟨⟨.even, 8, 10⟩, by decide⟩
  | 167 => ⟨⟨.even, 8, 11⟩, by decide⟩
  | 168 => ⟨⟨.even, 8, 12⟩, by decide⟩
  | 169 => ⟨⟨.even, 8, 13⟩, by decide⟩
  | 170 => ⟨⟨.even, 8, 14⟩, by decide⟩
  | 171 => ⟨⟨.even, 8, 15⟩, by decide⟩
  | 172 => ⟨⟨.even, 8, 16⟩, by decide⟩
  | 173 => ⟨⟨.even, 8, 17⟩, by decide⟩
  | 174 => ⟨⟨.even, 8, 18⟩, by decide⟩
  | 175 => ⟨⟨.even, 8, 19⟩, by decide⟩
  | 176 => ⟨⟨.even, 8, 20⟩, by decide⟩
  | 177 => ⟨⟨.even, 8, 21⟩, by decide⟩
  | 178 => ⟨⟨.even, 8, 22⟩, by decide⟩
  | 179 => ⟨⟨.even, 8, 23⟩, by decide⟩
  | 180 => ⟨⟨.even, 9, 9⟩, by decide⟩
  | 181 => ⟨⟨.even, 9, 10⟩, by decide⟩
  | 182 => ⟨⟨.even, 9, 11⟩, by decide⟩
  | 183 => ⟨⟨.even, 9, 12⟩, by decide⟩
  | 184 => ⟨⟨.even, 9, 13⟩, by decide⟩
  | 185 => ⟨⟨.even, 9, 14⟩, by decide⟩
  | 186 => ⟨⟨.even, 9, 15⟩, by decide⟩
  | 187 => ⟨⟨.even, 9, 16⟩, by decide⟩
  | 188 => ⟨⟨.even, 9, 17⟩, by decide⟩
  | 189 => ⟨⟨.even, 9, 18⟩, by decide⟩
  | 190 => ⟨⟨.even, 9, 19⟩, by decide⟩
  | 191 => ⟨⟨.even, 9, 20⟩, by decide⟩
  | 192 => ⟨⟨.even, 9, 21⟩, by decide⟩
  | 193 => ⟨⟨.even, 9, 22⟩, by decide⟩
  | 194 => ⟨⟨.even, 9, 23⟩, by decide⟩
  | 195 => ⟨⟨.even, 10, 10⟩, by decide⟩
  | 196 => ⟨⟨.even, 10, 11⟩, by decide⟩
  | 197 => ⟨⟨.even, 10, 12⟩, by decide⟩
  | 198 => ⟨⟨.even, 10, 13⟩, by decide⟩
  | 199 => ⟨⟨.even, 10, 14⟩, by decide⟩
  | 200 => ⟨⟨.even, 10, 15⟩, by decide⟩
  | 201 => ⟨⟨.even, 10, 16⟩, by decide⟩
  | 202 => ⟨⟨.even, 10, 17⟩, by decide⟩
  | 203 => ⟨⟨.even, 10, 18⟩, by decide⟩
  | 204 => ⟨⟨.even, 10, 19⟩, by decide⟩
  | 205 => ⟨⟨.even, 10, 20⟩, by decide⟩
  | 206 => ⟨⟨.even, 10, 21⟩, by decide⟩
  | 207 => ⟨⟨.even, 10, 22⟩, by decide⟩
  | 208 => ⟨⟨.even, 10, 23⟩, by decide⟩
  | 209 => ⟨⟨.even, 11, 11⟩, by decide⟩
  | 210 => ⟨⟨.even, 11, 12⟩, by decide⟩
  | 211 => ⟨⟨.even, 11, 13⟩, by decide⟩
  | 212 => ⟨⟨.even, 11, 14⟩, by decide⟩
  | 213 => ⟨⟨.even, 11, 15⟩, by decide⟩
  | 214 => ⟨⟨.even, 11, 16⟩, by decide⟩
  | 215 => ⟨⟨.even, 11, 17⟩, by decide⟩
  | 216 => ⟨⟨.even, 11, 18⟩, by decide⟩
  | 217 => ⟨⟨.even, 11, 19⟩, by decide⟩
  | 218 => ⟨⟨.even, 11, 20⟩, by decide⟩
  | 219 => ⟨⟨.even, 11, 21⟩, by decide⟩
  | 220 => ⟨⟨.even, 11, 22⟩, by decide⟩
  | 221 => ⟨⟨.even, 11, 23⟩, by decide⟩
  | 222 => ⟨⟨.even, 12, 12⟩, by decide⟩
  | 223 => ⟨⟨.even, 12, 13⟩, by decide⟩
  | 224 => ⟨⟨.even, 12, 14⟩, by decide⟩
  | 225 => ⟨⟨.even, 12, 15⟩, by decide⟩
  | 226 => ⟨⟨.even, 12, 16⟩, by decide⟩
  | 227 => ⟨⟨.even, 12, 17⟩, by decide⟩
  | 228 => ⟨⟨.even, 12, 18⟩, by decide⟩
  | 229 => ⟨⟨.even, 12, 19⟩, by decide⟩
  | 230 => ⟨⟨.even, 12, 20⟩, by decide⟩
  | 231 => ⟨⟨.even, 12, 21⟩, by decide⟩
  | 232 => ⟨⟨.even, 12, 22⟩, by decide⟩
  | 233 => ⟨⟨.even, 12, 23⟩, by decide⟩
  | 234 => ⟨⟨.even, 13, 13⟩, by decide⟩
  | 235 => ⟨⟨.even, 13, 14⟩, by decide⟩
  | 236 => ⟨⟨.even, 13, 15⟩, by decide⟩
  | 237 => ⟨⟨.even, 13, 16⟩, by decide⟩
  | 238 => ⟨⟨.even, 13, 17⟩, by decide⟩
  | 239 => ⟨⟨.even, 13, 18⟩, by decide⟩
  | 240 => ⟨⟨.even, 13, 19⟩, by decide⟩
  | 241 => ⟨⟨.even, 13, 20⟩, by decide⟩
  | 242 => ⟨⟨.even, 13, 21⟩, by decide⟩
  | 243 => ⟨⟨.even, 13, 22⟩, by decide⟩
  | 244 => ⟨⟨.even, 13, 23⟩, by decide⟩
  | 245 => ⟨⟨.even, 14, 14⟩, by decide⟩
  | 246 => ⟨⟨.even, 14, 15⟩, by decide⟩
  | 247 => ⟨⟨.even, 14, 16⟩, by decide⟩
  | 248 => ⟨⟨.even, 14, 17⟩, by decide⟩
  | 249 => ⟨⟨.even, 14, 18⟩, by decide⟩
  | 250 => ⟨⟨.even, 14, 19⟩, by decide⟩
  | 251 => ⟨⟨.even, 14, 20⟩, by decide⟩
  | 252 => ⟨⟨.even, 14, 21⟩, by decide⟩
  | 253 => ⟨⟨.even, 14, 22⟩, by decide⟩
  | 254 => ⟨⟨.even, 14, 23⟩, by decide⟩
  | 255 => ⟨⟨.even, 15, 15⟩, by decide⟩
  | 256 => ⟨⟨.even, 15, 16⟩, by decide⟩
  | 257 => ⟨⟨.even, 15, 17⟩, by decide⟩
  | 258 => ⟨⟨.even, 15, 18⟩, by decide⟩
  | 259 => ⟨⟨.even, 15, 19⟩, by decide⟩
  | 260 => ⟨⟨.even, 15, 20⟩, by decide⟩
  | 261 => ⟨⟨.even, 15, 21⟩, by decide⟩
  | 262 => ⟨⟨.even, 15, 22⟩, by decide⟩
  | 263 => ⟨⟨.even, 15, 23⟩, by decide⟩
  | 264 => ⟨⟨.even, 16, 16⟩, by decide⟩
  | 265 => ⟨⟨.even, 16, 17⟩, by decide⟩
  | 266 => ⟨⟨.even, 16, 18⟩, by decide⟩
  | 267 => ⟨⟨.even, 16, 19⟩, by decide⟩
  | 268 => ⟨⟨.even, 16, 20⟩, by decide⟩
  | 269 => ⟨⟨.even, 16, 21⟩, by decide⟩
  | 270 => ⟨⟨.even, 16, 22⟩, by decide⟩
  | 271 => ⟨⟨.even, 16, 23⟩, by decide⟩
  | 272 => ⟨⟨.even, 17, 17⟩, by decide⟩
  | 273 => ⟨⟨.even, 17, 18⟩, by decide⟩
  | 274 => ⟨⟨.even, 17, 19⟩, by decide⟩
  | 275 => ⟨⟨.even, 17, 20⟩, by decide⟩
  | 276 => ⟨⟨.even, 17, 21⟩, by decide⟩
  | 277 => ⟨⟨.even, 17, 22⟩, by decide⟩
  | 278 => ⟨⟨.even, 17, 23⟩, by decide⟩
  | 279 => ⟨⟨.even, 18, 18⟩, by decide⟩
  | 280 => ⟨⟨.even, 18, 19⟩, by decide⟩
  | 281 => ⟨⟨.even, 18, 20⟩, by decide⟩
  | 282 => ⟨⟨.even, 18, 21⟩, by decide⟩
  | 283 => ⟨⟨.even, 18, 22⟩, by decide⟩
  | 284 => ⟨⟨.even, 18, 23⟩, by decide⟩
  | 285 => ⟨⟨.even, 19, 19⟩, by decide⟩
  | 286 => ⟨⟨.even, 19, 20⟩, by decide⟩
  | 287 => ⟨⟨.even, 19, 21⟩, by decide⟩
  | 288 => ⟨⟨.even, 19, 22⟩, by decide⟩
  | 289 => ⟨⟨.even, 19, 23⟩, by decide⟩
  | 290 => ⟨⟨.even, 20, 20⟩, by decide⟩
  | 291 => ⟨⟨.even, 20, 21⟩, by decide⟩
  | 292 => ⟨⟨.even, 20, 22⟩, by decide⟩
  | 293 => ⟨⟨.even, 20, 23⟩, by decide⟩
  | 294 => ⟨⟨.even, 21, 21⟩, by decide⟩
  | 295 => ⟨⟨.even, 21, 22⟩, by decide⟩
  | 296 => ⟨⟨.even, 21, 23⟩, by decide⟩
  | 297 => ⟨⟨.even, 22, 22⟩, by decide⟩
  | 298 => ⟨⟨.even, 22, 23⟩, by decide⟩
  | 299 => ⟨⟨.even, 23, 23⟩, by decide⟩
  | 300 => ⟨⟨.odd, 0, 0⟩, by decide⟩
  | 301 => ⟨⟨.odd, 0, 1⟩, by decide⟩
  | 302 => ⟨⟨.odd, 0, 2⟩, by decide⟩
  | 303 => ⟨⟨.odd, 0, 3⟩, by decide⟩
  | 304 => ⟨⟨.odd, 0, 4⟩, by decide⟩
  | 305 => ⟨⟨.odd, 0, 5⟩, by decide⟩
  | 306 => ⟨⟨.odd, 0, 6⟩, by decide⟩
  | 307 => ⟨⟨.odd, 0, 7⟩, by decide⟩
  | 308 => ⟨⟨.odd, 0, 8⟩, by decide⟩
  | 309 => ⟨⟨.odd, 0, 9⟩, by decide⟩
  | 310 => ⟨⟨.odd, 0, 10⟩, by decide⟩
  | 311 => ⟨⟨.odd, 0, 11⟩, by decide⟩
  | 312 => ⟨⟨.odd, 0, 12⟩, by decide⟩
  | 313 => ⟨⟨.odd, 0, 13⟩, by decide⟩
  | 314 => ⟨⟨.odd, 0, 14⟩, by decide⟩
  | 315 => ⟨⟨.odd, 0, 15⟩, by decide⟩
  | 316 => ⟨⟨.odd, 0, 16⟩, by decide⟩
  | 317 => ⟨⟨.odd, 0, 17⟩, by decide⟩
  | 318 => ⟨⟨.odd, 0, 18⟩, by decide⟩
  | 319 => ⟨⟨.odd, 0, 19⟩, by decide⟩
  | 320 => ⟨⟨.odd, 0, 20⟩, by decide⟩
  | 321 => ⟨⟨.odd, 0, 21⟩, by decide⟩
  | 322 => ⟨⟨.odd, 0, 22⟩, by decide⟩
  | 323 => ⟨⟨.odd, 0, 23⟩, by decide⟩
  | 324 => ⟨⟨.odd, 1, 1⟩, by decide⟩
  | 325 => ⟨⟨.odd, 1, 2⟩, by decide⟩
  | 326 => ⟨⟨.odd, 1, 3⟩, by decide⟩
  | 327 => ⟨⟨.odd, 1, 4⟩, by decide⟩
  | 328 => ⟨⟨.odd, 1, 5⟩, by decide⟩
  | 329 => ⟨⟨.odd, 1, 6⟩, by decide⟩
  | 330 => ⟨⟨.odd, 1, 7⟩, by decide⟩
  | 331 => ⟨⟨.odd, 1, 8⟩, by decide⟩
  | 332 => ⟨⟨.odd, 1, 9⟩, by decide⟩
  | 333 => ⟨⟨.odd, 1, 10⟩, by decide⟩
  | 334 => ⟨⟨.odd, 1, 11⟩, by decide⟩
  | 335 => ⟨⟨.odd, 1, 12⟩, by decide⟩
  | 336 => ⟨⟨.odd, 1, 13⟩, by decide⟩
  | 337 => ⟨⟨.odd, 1, 14⟩, by decide⟩
  | 338 => ⟨⟨.odd, 1, 15⟩, by decide⟩
  | 339 => ⟨⟨.odd, 1, 16⟩, by decide⟩
  | 340 => ⟨⟨.odd, 1, 17⟩, by decide⟩
  | 341 => ⟨⟨.odd, 1, 18⟩, by decide⟩
  | 342 => ⟨⟨.odd, 1, 19⟩, by decide⟩
  | 343 => ⟨⟨.odd, 1, 20⟩, by decide⟩
  | 344 => ⟨⟨.odd, 1, 21⟩, by decide⟩
  | 345 => ⟨⟨.odd, 1, 22⟩, by decide⟩
  | 346 => ⟨⟨.odd, 1, 23⟩, by decide⟩
  | 347 => ⟨⟨.odd, 2, 2⟩, by decide⟩
  | 348 => ⟨⟨.odd, 2, 3⟩, by decide⟩
  | 349 => ⟨⟨.odd, 2, 4⟩, by decide⟩
  | 350 => ⟨⟨.odd, 2, 5⟩, by decide⟩
  | 351 => ⟨⟨.odd, 2, 6⟩, by decide⟩
  | 352 => ⟨⟨.odd, 2, 7⟩, by decide⟩
  | 353 => ⟨⟨.odd, 2, 8⟩, by decide⟩
  | 354 => ⟨⟨.odd, 2, 9⟩, by decide⟩
  | 355 => ⟨⟨.odd, 2, 10⟩, by decide⟩
  | 356 => ⟨⟨.odd, 2, 11⟩, by decide⟩
  | 357 => ⟨⟨.odd, 2, 12⟩, by decide⟩
  | 358 => ⟨⟨.odd, 2, 13⟩, by decide⟩
  | 359 => ⟨⟨.odd, 2, 14⟩, by decide⟩
  | 360 => ⟨⟨.odd, 2, 15⟩, by decide⟩
  | 361 => ⟨⟨.odd, 2, 16⟩, by decide⟩
  | 362 => ⟨⟨.odd, 2, 17⟩, by decide⟩
  | 363 => ⟨⟨.odd, 2, 18⟩, by decide⟩
  | 364 => ⟨⟨.odd, 2, 19⟩, by decide⟩
  | 365 => ⟨⟨.odd, 2, 20⟩, by decide⟩
  | 366 => ⟨⟨.odd, 2, 21⟩, by decide⟩
  | 367 => ⟨⟨.odd, 2, 22⟩, by decide⟩
  | 368 => ⟨⟨.odd, 2, 23⟩, by decide⟩
  | 369 => ⟨⟨.odd, 3, 3⟩, by decide⟩
  | 370 => ⟨⟨.odd, 3, 4⟩, by decide⟩
  | 371 => ⟨⟨.odd, 3, 5⟩, by decide⟩
  | 372 => ⟨⟨.odd, 3, 6⟩, by decide⟩
  | 373 => ⟨⟨.odd, 3, 7⟩, by decide⟩
  | 374 => ⟨⟨.odd, 3, 8⟩, by decide⟩
  | 375 => ⟨⟨.odd, 3, 9⟩, by decide⟩
  | 376 => ⟨⟨.odd, 3, 10⟩, by decide⟩
  | 377 => ⟨⟨.odd, 3, 11⟩, by decide⟩
  | 378 => ⟨⟨.odd, 3, 12⟩, by decide⟩
  | 379 => ⟨⟨.odd, 3, 13⟩, by decide⟩
  | 380 => ⟨⟨.odd, 3, 14⟩, by decide⟩
  | 381 => ⟨⟨.odd, 3, 15⟩, by decide⟩
  | 382 => ⟨⟨.odd, 3, 16⟩, by decide⟩
  | 383 => ⟨⟨.odd, 3, 17⟩, by decide⟩
  | 384 => ⟨⟨.odd, 3, 18⟩, by decide⟩
  | 385 => ⟨⟨.odd, 3, 19⟩, by decide⟩
  | 386 => ⟨⟨.odd, 3, 20⟩, by decide⟩
  | 387 => ⟨⟨.odd, 3, 21⟩, by decide⟩
  | 388 => ⟨⟨.odd, 3, 22⟩, by decide⟩
  | 389 => ⟨⟨.odd, 3, 23⟩, by decide⟩
  | 390 => ⟨⟨.odd, 4, 4⟩, by decide⟩
  | 391 => ⟨⟨.odd, 4, 5⟩, by decide⟩
  | 392 => ⟨⟨.odd, 4, 6⟩, by decide⟩
  | 393 => ⟨⟨.odd, 4, 7⟩, by decide⟩
  | 394 => ⟨⟨.odd, 4, 8⟩, by decide⟩
  | 395 => ⟨⟨.odd, 4, 9⟩, by decide⟩
  | 396 => ⟨⟨.odd, 4, 10⟩, by decide⟩
  | 397 => ⟨⟨.odd, 4, 11⟩, by decide⟩
  | 398 => ⟨⟨.odd, 4, 12⟩, by decide⟩
  | 399 => ⟨⟨.odd, 4, 13⟩, by decide⟩
  | 400 => ⟨⟨.odd, 4, 14⟩, by decide⟩
  | 401 => ⟨⟨.odd, 4, 15⟩, by decide⟩
  | 402 => ⟨⟨.odd, 4, 16⟩, by decide⟩
  | 403 => ⟨⟨.odd, 4, 17⟩, by decide⟩
  | 404 => ⟨⟨.odd, 4, 18⟩, by decide⟩
  | 405 => ⟨⟨.odd, 4, 19⟩, by decide⟩
  | 406 => ⟨⟨.odd, 4, 20⟩, by decide⟩
  | 407 => ⟨⟨.odd, 4, 21⟩, by decide⟩
  | 408 => ⟨⟨.odd, 4, 22⟩, by decide⟩
  | 409 => ⟨⟨.odd, 4, 23⟩, by decide⟩
  | 410 => ⟨⟨.odd, 5, 5⟩, by decide⟩
  | 411 => ⟨⟨.odd, 5, 6⟩, by decide⟩
  | 412 => ⟨⟨.odd, 5, 7⟩, by decide⟩
  | 413 => ⟨⟨.odd, 5, 8⟩, by decide⟩
  | 414 => ⟨⟨.odd, 5, 9⟩, by decide⟩
  | 415 => ⟨⟨.odd, 5, 10⟩, by decide⟩
  | 416 => ⟨⟨.odd, 5, 11⟩, by decide⟩
  | 417 => ⟨⟨.odd, 5, 12⟩, by decide⟩
  | 418 => ⟨⟨.odd, 5, 13⟩, by decide⟩
  | 419 => ⟨⟨.odd, 5, 14⟩, by decide⟩
  | 420 => ⟨⟨.odd, 5, 15⟩, by decide⟩
  | 421 => ⟨⟨.odd, 5, 16⟩, by decide⟩
  | 422 => ⟨⟨.odd, 5, 17⟩, by decide⟩
  | 423 => ⟨⟨.odd, 5, 18⟩, by decide⟩
  | 424 => ⟨⟨.odd, 5, 19⟩, by decide⟩
  | 425 => ⟨⟨.odd, 5, 20⟩, by decide⟩
  | 426 => ⟨⟨.odd, 5, 21⟩, by decide⟩
  | 427 => ⟨⟨.odd, 5, 22⟩, by decide⟩
  | 428 => ⟨⟨.odd, 5, 23⟩, by decide⟩
  | 429 => ⟨⟨.odd, 6, 6⟩, by decide⟩
  | 430 => ⟨⟨.odd, 6, 7⟩, by decide⟩
  | 431 => ⟨⟨.odd, 6, 8⟩, by decide⟩
  | 432 => ⟨⟨.odd, 6, 9⟩, by decide⟩
  | 433 => ⟨⟨.odd, 6, 10⟩, by decide⟩
  | 434 => ⟨⟨.odd, 6, 11⟩, by decide⟩
  | 435 => ⟨⟨.odd, 6, 12⟩, by decide⟩
  | 436 => ⟨⟨.odd, 6, 13⟩, by decide⟩
  | 437 => ⟨⟨.odd, 6, 14⟩, by decide⟩
  | 438 => ⟨⟨.odd, 6, 15⟩, by decide⟩
  | 439 => ⟨⟨.odd, 6, 16⟩, by decide⟩
  | 440 => ⟨⟨.odd, 6, 17⟩, by decide⟩
  | 441 => ⟨⟨.odd, 6, 18⟩, by decide⟩
  | 442 => ⟨⟨.odd, 6, 19⟩, by decide⟩
  | 443 => ⟨⟨.odd, 6, 20⟩, by decide⟩
  | 444 => ⟨⟨.odd, 6, 21⟩, by decide⟩
  | 445 => ⟨⟨.odd, 6, 22⟩, by decide⟩
  | 446 => ⟨⟨.odd, 6, 23⟩, by decide⟩
  | 447 => ⟨⟨.odd, 7, 7⟩, by decide⟩
  | 448 => ⟨⟨.odd, 7, 8⟩, by decide⟩
  | 449 => ⟨⟨.odd, 7, 9⟩, by decide⟩
  | 450 => ⟨⟨.odd, 7, 10⟩, by decide⟩
  | 451 => ⟨⟨.odd, 7, 11⟩, by decide⟩
  | 452 => ⟨⟨.odd, 7, 12⟩, by decide⟩
  | 453 => ⟨⟨.odd, 7, 13⟩, by decide⟩
  | 454 => ⟨⟨.odd, 7, 14⟩, by decide⟩
  | 455 => ⟨⟨.odd, 7, 15⟩, by decide⟩
  | 456 => ⟨⟨.odd, 7, 16⟩, by decide⟩
  | 457 => ⟨⟨.odd, 7, 17⟩, by decide⟩
  | 458 => ⟨⟨.odd, 7, 18⟩, by decide⟩
  | 459 => ⟨⟨.odd, 7, 19⟩, by decide⟩
  | 460 => ⟨⟨.odd, 7, 20⟩, by decide⟩
  | 461 => ⟨⟨.odd, 7, 21⟩, by decide⟩
  | 462 => ⟨⟨.odd, 7, 22⟩, by decide⟩
  | 463 => ⟨⟨.odd, 7, 23⟩, by decide⟩
  | 464 => ⟨⟨.odd, 8, 8⟩, by decide⟩
  | 465 => ⟨⟨.odd, 8, 9⟩, by decide⟩
  | 466 => ⟨⟨.odd, 8, 10⟩, by decide⟩
  | 467 => ⟨⟨.odd, 8, 11⟩, by decide⟩
  | 468 => ⟨⟨.odd, 8, 12⟩, by decide⟩
  | 469 => ⟨⟨.odd, 8, 13⟩, by decide⟩
  | 470 => ⟨⟨.odd, 8, 14⟩, by decide⟩
  | 471 => ⟨⟨.odd, 8, 15⟩, by decide⟩
  | 472 => ⟨⟨.odd, 8, 16⟩, by decide⟩
  | 473 => ⟨⟨.odd, 8, 17⟩, by decide⟩
  | 474 => ⟨⟨.odd, 8, 18⟩, by decide⟩
  | 475 => ⟨⟨.odd, 8, 19⟩, by decide⟩
  | 476 => ⟨⟨.odd, 8, 20⟩, by decide⟩
  | 477 => ⟨⟨.odd, 8, 21⟩, by decide⟩
  | 478 => ⟨⟨.odd, 8, 22⟩, by decide⟩
  | 479 => ⟨⟨.odd, 8, 23⟩, by decide⟩
  | 480 => ⟨⟨.odd, 9, 9⟩, by decide⟩
  | 481 => ⟨⟨.odd, 9, 10⟩, by decide⟩
  | 482 => ⟨⟨.odd, 9, 11⟩, by decide⟩
  | 483 => ⟨⟨.odd, 9, 12⟩, by decide⟩
  | 484 => ⟨⟨.odd, 9, 13⟩, by decide⟩
  | 485 => ⟨⟨.odd, 9, 14⟩, by decide⟩
  | 486 => ⟨⟨.odd, 9, 15⟩, by decide⟩
  | 487 => ⟨⟨.odd, 9, 16⟩, by decide⟩
  | 488 => ⟨⟨.odd, 9, 17⟩, by decide⟩
  | 489 => ⟨⟨.odd, 9, 18⟩, by decide⟩
  | 490 => ⟨⟨.odd, 9, 19⟩, by decide⟩
  | 491 => ⟨⟨.odd, 9, 20⟩, by decide⟩
  | 492 => ⟨⟨.odd, 9, 21⟩, by decide⟩
  | 493 => ⟨⟨.odd, 9, 22⟩, by decide⟩
  | 494 => ⟨⟨.odd, 9, 23⟩, by decide⟩
  | 495 => ⟨⟨.odd, 10, 10⟩, by decide⟩
  | 496 => ⟨⟨.odd, 10, 11⟩, by decide⟩
  | 497 => ⟨⟨.odd, 10, 12⟩, by decide⟩
  | 498 => ⟨⟨.odd, 10, 13⟩, by decide⟩
  | 499 => ⟨⟨.odd, 10, 14⟩, by decide⟩
  | 500 => ⟨⟨.odd, 10, 15⟩, by decide⟩
  | 501 => ⟨⟨.odd, 10, 16⟩, by decide⟩
  | 502 => ⟨⟨.odd, 10, 17⟩, by decide⟩
  | 503 => ⟨⟨.odd, 10, 18⟩, by decide⟩
  | 504 => ⟨⟨.odd, 10, 19⟩, by decide⟩
  | 505 => ⟨⟨.odd, 10, 20⟩, by decide⟩
  | 506 => ⟨⟨.odd, 10, 21⟩, by decide⟩
  | 507 => ⟨⟨.odd, 10, 22⟩, by decide⟩
  | 508 => ⟨⟨.odd, 10, 23⟩, by decide⟩
  | 509 => ⟨⟨.odd, 11, 11⟩, by decide⟩
  | 510 => ⟨⟨.odd, 11, 12⟩, by decide⟩
  | 511 => ⟨⟨.odd, 11, 13⟩, by decide⟩
  | 512 => ⟨⟨.odd, 11, 14⟩, by decide⟩
  | 513 => ⟨⟨.odd, 11, 15⟩, by decide⟩
  | 514 => ⟨⟨.odd, 11, 16⟩, by decide⟩
  | 515 => ⟨⟨.odd, 11, 17⟩, by decide⟩
  | 516 => ⟨⟨.odd, 11, 18⟩, by decide⟩
  | 517 => ⟨⟨.odd, 11, 19⟩, by decide⟩
  | 518 => ⟨⟨.odd, 11, 20⟩, by decide⟩
  | 519 => ⟨⟨.odd, 11, 21⟩, by decide⟩
  | 520 => ⟨⟨.odd, 11, 22⟩, by decide⟩
  | 521 => ⟨⟨.odd, 11, 23⟩, by decide⟩
  | 522 => ⟨⟨.odd, 12, 12⟩, by decide⟩
  | 523 => ⟨⟨.odd, 12, 13⟩, by decide⟩
  | 524 => ⟨⟨.odd, 12, 14⟩, by decide⟩
  | 525 => ⟨⟨.odd, 12, 15⟩, by decide⟩
  | 526 => ⟨⟨.odd, 12, 16⟩, by decide⟩
  | 527 => ⟨⟨.odd, 12, 17⟩, by decide⟩
  | 528 => ⟨⟨.odd, 12, 18⟩, by decide⟩
  | 529 => ⟨⟨.odd, 12, 19⟩, by decide⟩
  | 530 => ⟨⟨.odd, 12, 20⟩, by decide⟩
  | 531 => ⟨⟨.odd, 12, 21⟩, by decide⟩
  | 532 => ⟨⟨.odd, 12, 22⟩, by decide⟩
  | 533 => ⟨⟨.odd, 12, 23⟩, by decide⟩
  | 534 => ⟨⟨.odd, 13, 13⟩, by decide⟩
  | 535 => ⟨⟨.odd, 13, 14⟩, by decide⟩
  | 536 => ⟨⟨.odd, 13, 15⟩, by decide⟩
  | 537 => ⟨⟨.odd, 13, 16⟩, by decide⟩
  | 538 => ⟨⟨.odd, 13, 17⟩, by decide⟩
  | 539 => ⟨⟨.odd, 13, 18⟩, by decide⟩
  | 540 => ⟨⟨.odd, 13, 19⟩, by decide⟩
  | 541 => ⟨⟨.odd, 13, 20⟩, by decide⟩
  | 542 => ⟨⟨.odd, 13, 21⟩, by decide⟩
  | 543 => ⟨⟨.odd, 13, 22⟩, by decide⟩
  | 544 => ⟨⟨.odd, 13, 23⟩, by decide⟩
  | 545 => ⟨⟨.odd, 14, 14⟩, by decide⟩
  | 546 => ⟨⟨.odd, 14, 15⟩, by decide⟩
  | 547 => ⟨⟨.odd, 14, 16⟩, by decide⟩
  | 548 => ⟨⟨.odd, 14, 17⟩, by decide⟩
  | 549 => ⟨⟨.odd, 14, 18⟩, by decide⟩
  | 550 => ⟨⟨.odd, 14, 19⟩, by decide⟩
  | 551 => ⟨⟨.odd, 14, 20⟩, by decide⟩
  | 552 => ⟨⟨.odd, 14, 21⟩, by decide⟩
  | 553 => ⟨⟨.odd, 14, 22⟩, by decide⟩
  | 554 => ⟨⟨.odd, 14, 23⟩, by decide⟩
  | 555 => ⟨⟨.odd, 15, 15⟩, by decide⟩
  | 556 => ⟨⟨.odd, 15, 16⟩, by decide⟩
  | 557 => ⟨⟨.odd, 15, 17⟩, by decide⟩
  | 558 => ⟨⟨.odd, 15, 18⟩, by decide⟩
  | 559 => ⟨⟨.odd, 15, 19⟩, by decide⟩
  | 560 => ⟨⟨.odd, 15, 20⟩, by decide⟩
  | 561 => ⟨⟨.odd, 15, 21⟩, by decide⟩
  | 562 => ⟨⟨.odd, 15, 22⟩, by decide⟩
  | 563 => ⟨⟨.odd, 15, 23⟩, by decide⟩
  | 564 => ⟨⟨.odd, 16, 16⟩, by decide⟩
  | 565 => ⟨⟨.odd, 16, 17⟩, by decide⟩
  | 566 => ⟨⟨.odd, 16, 18⟩, by decide⟩
  | 567 => ⟨⟨.odd, 16, 19⟩, by decide⟩
  | 568 => ⟨⟨.odd, 16, 20⟩, by decide⟩
  | 569 => ⟨⟨.odd, 16, 21⟩, by decide⟩
  | 570 => ⟨⟨.odd, 16, 22⟩, by decide⟩
  | 571 => ⟨⟨.odd, 16, 23⟩, by decide⟩
  | 572 => ⟨⟨.odd, 17, 17⟩, by decide⟩
  | 573 => ⟨⟨.odd, 17, 18⟩, by decide⟩
  | 574 => ⟨⟨.odd, 17, 19⟩, by decide⟩
  | 575 => ⟨⟨.odd, 17, 20⟩, by decide⟩
  | 576 => ⟨⟨.odd, 17, 21⟩, by decide⟩
  | 577 => ⟨⟨.odd, 17, 22⟩, by decide⟩
  | 578 => ⟨⟨.odd, 17, 23⟩, by decide⟩
  | 579 => ⟨⟨.odd, 18, 18⟩, by decide⟩
  | 580 => ⟨⟨.odd, 18, 19⟩, by decide⟩
  | 581 => ⟨⟨.odd, 18, 20⟩, by decide⟩
  | 582 => ⟨⟨.odd, 18, 21⟩, by decide⟩
  | 583 => ⟨⟨.odd, 18, 22⟩, by decide⟩
  | 584 => ⟨⟨.odd, 18, 23⟩, by decide⟩
  | 585 => ⟨⟨.odd, 19, 19⟩, by decide⟩
  | 586 => ⟨⟨.odd, 19, 20⟩, by decide⟩
  | 587 => ⟨⟨.odd, 19, 21⟩, by decide⟩
  | 588 => ⟨⟨.odd, 19, 22⟩, by decide⟩
  | 589 => ⟨⟨.odd, 19, 23⟩, by decide⟩
  | 590 => ⟨⟨.odd, 20, 20⟩, by decide⟩
  | 591 => ⟨⟨.odd, 20, 21⟩, by decide⟩
  | 592 => ⟨⟨.odd, 20, 22⟩, by decide⟩
  | 593 => ⟨⟨.odd, 20, 23⟩, by decide⟩
  | 594 => ⟨⟨.odd, 21, 21⟩, by decide⟩
  | 595 => ⟨⟨.odd, 21, 22⟩, by decide⟩
  | 596 => ⟨⟨.odd, 21, 23⟩, by decide⟩
  | 597 => ⟨⟨.odd, 22, 22⟩, by decide⟩
  | 598 => ⟨⟨.odd, 22, 23⟩, by decide⟩
  | 599 => ⟨⟨.odd, 23, 23⟩, by decide⟩
  | _ => ⟨⟨.even, 0, 0⟩, by decide⟩

/-- The explicit table restricted to its 600 meaningful rows. -/
def p2UpperEntryAt (k : Fin 600) : P2UpperEntryIndex :=
  p2UpperEntryAtNat k.val

/-- Row-major offset of the upper-triangular row `i`. -/
def p2UpperRowOffset (i : ℕ) : ℕ :=
  i * 24 - i * (i - 1) / 2

/-- Arithmetic inverse code for an upper-triangular tagged entry. -/
def p2UpperEntryCode (e : P2UpperEntryIndex) : ℕ :=
  (match e.val.block with | .even => 0 | .odd => 300) +
    p2UpperRowOffset e.val.row.val +
      (e.val.col.val - e.val.row.val)

set_option maxRecDepth 4096 in
-- Kernel evaluation checks all 600 generated rows of the inverse table.
theorem p2UpperEntryCode_at (k : Fin 600) :
    p2UpperEntryCode (p2UpperEntryAt k) = k.val := by
  decide +revert

theorem p2UpperEntryAt_injective : Function.Injective p2UpperEntryAt := by
  intro a b hab
  have hcode := congrArg p2UpperEntryCode hab
  rw [p2UpperEntryCode_at, p2UpperEntryCode_at] at hcode
  exact Fin.ext hcode

theorem p2UpperEntryAt_bijective : Function.Bijective p2UpperEntryAt := by
  apply (Fintype.bijective_iff_injective_and_card p2UpperEntryAt).2
  exact ⟨p2UpperEntryAt_injective, by simp [card_p2UpperEntryIndex]⟩

/-- Kernel-verified equivalence between generated rows and certificate entries. -/
noncomputable def p2UpperEntryEquiv : Fin 600 ≃ P2UpperEntryIndex :=
  Equiv.ofBijective p2UpperEntryAt p2UpperEntryAt_bijective

/-- A generated proof table indexed by the explicit 600-row order. -/
def P2GeneratedEntryEnclosures : Prop :=
  ∀ k : Fin 600,
    p2StoredLower (p2UpperEntryAt k).val ≤
        p2ScalarEntry (p2UpperEntryAt k).val ∧
      p2ScalarEntry (p2UpperEntryAt k).val ≤
        p2StoredUpper (p2UpperEntryAt k).val

/-- Center-radius version of the generated 600-row proof table. -/
def P2GeneratedEntryCenterCertificate : Prop :=
  ∀ k : Fin 600,
    |p2ScalarEntry (p2UpperEntryAt k).val -
      p2StoredCenter (p2UpperEntryAt k).val| ≤ p2StoredRadius

theorem p2UpperEntryEnclosures_of_generated
    (h : P2GeneratedEntryEnclosures) : P2UpperEntryEnclosures := by
  intro e
  have hk := h (p2UpperEntryEquiv.symm e)
  have hidx : p2UpperEntryAt (p2UpperEntryEquiv.symm e) = e :=
    p2UpperEntryEquiv.apply_symm_apply e
  rwa [hidx] at hk

theorem p2GeneratedEntryEnclosures_of_upper
    (h : P2UpperEntryEnclosures) : P2GeneratedEntryEnclosures := by
  intro k
  exact h (p2UpperEntryAt k)

theorem p2UpperEntryCenterCertificate_of_generated
    (h : P2GeneratedEntryCenterCertificate) :
    P2UpperEntryCenterCertificate := by
  intro e
  have hk := h (p2UpperEntryEquiv.symm e)
  have hidx : p2UpperEntryAt (p2UpperEntryEquiv.symm e) = e :=
    p2UpperEntryEquiv.apply_symm_apply e
  rwa [hidx] at hk

/-- Final clipped endpoint consuming a generated 600-row interval table. -/
theorem p2_clipped_endpoint_of_generated_entry_enclosures
    (h : P2GeneratedEntryEnclosures)
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  exact p2_clipped_endpoint_of_upper_entry_enclosures
    (p2UpperEntryEnclosures_of_generated h) hf

/-- Final clipped endpoint consuming generated center-radius proofs. -/
theorem p2_clipped_endpoint_of_generated_center_certificate
    (h : P2GeneratedEntryCenterCertificate)
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  exact p2_clipped_endpoint_of_upper_center_certificate
    (p2UpperEntryCenterCertificate_of_generated h) hf

end

end RHP2Bridge
