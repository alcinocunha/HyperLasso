# hyperltl-bmc

(Complete) Bounded model checker for HyperLTL

## Usage
To run the bounded model checker, use the following command:

```bash
python bmc.py <model_file.smv> <trace_length>
```

Replace `<model_file.smv>` with the path to your SMV model file and `<trace_length>` with the exact length of the traces that will be checked.
See example SMV files in the `examples/` directory, including how to specify HyperLTL properties in the `HLTLSPEC` section.
