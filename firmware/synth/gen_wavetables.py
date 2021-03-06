import math

def PrintSineTable(max_amount, table_length, format_string, numbers_per_line = 8):
    for x in range(table_length):
        # Compute the phase scaled out to the length of the table.
        phase = 2.0 * math.pi * (x / float(table_length))

        # Scale the normal -1.0 to 1.0 output to 0 to max_amount.
        val = (1.0 - (math.cos(phase) + 1.0) / 2.0) * max_amount

        print(format_string % int(round(val)), end="")
        if (x + 1) % numbers_per_line == 0:
            print()

def PrintSawtoothTable(max_amount, table_length, format_string, numbers_per_line = 8):
    for x in range(table_length):
        val = x / table_length  * max_amount

        print(format_string % int(round(val)), end="")
        if (x + 1) % numbers_per_line == 0:
            print()

print("// THIS FILE WAS AUTO-GENERATED BY GEN_WAVETABLES.PY - DO NOT EDIT\n")
print("#include <stdint.h>\n")

print("const uint8_t SINE_TABLE_UINT8[256] = {")
PrintSineTable((1 << 8) - 1, 1 << 8, "0x%02x, ")
print("};\n")

print("const uint16_t SINE_TABLE_UINT16[256] = {")
PrintSineTable((1 << 16) - 1, 1 << 8, "0x%04x, ")
print("};\n")

print("const uint16_t SAWTOOTH_TABLE_UINT16[256] = {")
PrintSawtoothTable((1 << 16) - 1, 1 << 8, "0x%04x, ")
print("};\n")

print("const uint32_t SINE_TABLE_UINT32[256] = {")
PrintSineTable((1 << 32) - 1, 1 << 8, "0x%08x, ", 4)
print("};\n")
