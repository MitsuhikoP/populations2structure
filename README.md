# populations2structure
covert populations.structure by stacks to structure format and main parameter files

```
K=3
populations2structure -s populations.structure -o populations2.structure${K} -k ${K} > mainparams${K}
structure -m mainparams${K} -e extraparams -i populations2.structure${K} -o output_k${K} > out_step${K}
```

If you would like to exchange the order of samples, use `-l` option and reordering list.
