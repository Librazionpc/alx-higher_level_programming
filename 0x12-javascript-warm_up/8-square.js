#!/usr/bin/node
if (process.argv.length === 2)
        console.log("Missing size")
else
{
        const x = parseInt(process.argv[2]);
        if (x)
        {
                for (let i = 0; i < x; i++)
		{
			let square = "";
                        for (let i = 0; i < x; i++)
				square += "X";
			console.log(square)
		}

        }
        else
                console.log("Missing size");
}
