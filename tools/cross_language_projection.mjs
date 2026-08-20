import { readFileSync } from "node:fs";

const fixture = JSON.parse(readFileSync(process.argv[2], "utf8"));
const identity = { composition: fixture.semantic.block, target: fixture.semantic.block };
const operations = fixture.semantic.operations;
const vectors = fixture.expressions.map((expression) => ({
  identity,
  operations,
  visualLanguage: expression.visualLanguage,
}));
process.stdout.write(JSON.stringify({ identity, operations, vectors }));
