#!/usr/bin/node
const array1 = [];
if (process.argv.length === 2 || process.argv[2] === '1')
        console.log(0);
else
{
	const args = process.argv
	.map(Number)
	.slice(2, process.argv.length)
	.sort((a, b) => a - b);
	console.log(args[args.length - 2]);
}
