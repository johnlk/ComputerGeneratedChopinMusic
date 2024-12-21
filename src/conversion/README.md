# MIDI <-> ASCII Conversion Tools

Command-line tools for converting between MIDI and ASCII text formats.

## Compilation 

```bash
gcc -o mid2asc mid2asc.c -lm
gcc -o asc2mid asc2mid.c -lm
```

## Usage

Convert MIDI to ASCII:
```bash
./mid2asc input.mid > output.txt
```

Convert ASCII back to MIDI:
```bash
./asc2mid input.txt > output.mid
```

### mid2asc Options

- `-c`: Output absolute crotchet timings
- `-f`: Output relative timings (from previous note)
- `-r`: Output raw delta timings
- `-s`: Output tracks separately

For example:
```bash
./mid2asc -s input.mid > separated_tracks.txt
```

## File Format Reference

The ASCII format represents MIDI events in a human-readable text format. Each line represents either a comment (starting with #) or an event.

Events must include:
- Time specification
- Track number (TR)
- Channel number (CH)
- Event type and parameters

Example event lines:
```
BA 1 CR 0 TR 0 CH 1 NT C' 1/2 von=80
BA 1 CR 1/2 TR 0 CH 1 NT E' 1/2 von=80
BA 2 CR 0 TR 0 CH 1 NT G' 1 von=80
```

For detailed format documentation, see the original instructions file. [Website here](https://www.archduke.org/midi/instrux.html)

