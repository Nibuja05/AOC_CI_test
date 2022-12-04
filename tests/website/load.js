const zeroPad = (num, places) => String(num).padStart(places, "0");

function createElement(type, parent, options = {}) {
	const item = document.createElement(type);
	if (options.id) item.id = options.id;
	if (options.classes) options.classes.map((c) => item.classList.add(c));
	if (options.content) item.innerHTML = options.content;
	parent.appendChild(item);
	return item;
}

// const BASE_PATH ="file:///C:/Users/anton/Programmieren/AOC_CI_test/tests/website/";
const BASE_PATH = "https://nibuja05.github.io/AOC_CI_test/";

async function loadDataForDay(day) {
	try {
		const request = await fetch(BASE_PATH + `data/${zeroPad(day, 2)}.json`);
		const result = await request.json();
		return result;
	} catch (error) {
		console.log(error);
		console.log(`No existing data for ${day}`);
	}
	return undefined;
}

async function loadDays() {
	for (let i = 1; i <= 24; i++) {
		dayData = await loadDataForDay(i);

		createDay(i, dayData);
	}
	createElement("div", document.getElementById("content"), {
		classes: ["placeholder"],
	});
}

function prepareDays() {
	const nav = document.getElementById("nav");
	for (let i = 1; i <= 24; i++) {
		const newDay = createElement("div", nav, {
			id: `nav-day${i}`,
			classes: ["day", "inactive"],
		});
		const dayLink = createElement("a", newDay, { content: i });
		dayLink.href = `#day${i}`;
	}
}

function createDay(index, data) {
	const newDay = document.getElementById(`nav-day${index}`);

	const count = Object.keys(data).length;
	if (data && count > 0) {
		newDay.classList.remove("inactive");

		const resultContainer = document.getElementById("content");

		const result = createElement("div", resultContainer, {
			classes: ["result"],
			id: `day${index}-data`,
		});
		createElement("div", result, {
			id: `day${index}`,
			classes: ["anchor"],
		});

		const header = createElement("div", result, { classes: ["header"] });
		createElement("p", header, { content: `Day ${index}` });

		const validCount = Object.values(data).filter(
			(entry) => entry.valid == "true"
		).length;
		createElement("div", header, {
			classes: ["counts"],
			content: `Solutions: ${validCount}/${count}`,
		});

		const solutions = createElement("div", result, {
			classes: ["solutions"],
		});

		const MAX_VAL = 0;

		let maxValues = [];
		for (let task = 1; task <= 2; task++) {
			maxValues.push(
				Math.max(
					...Object.values(data).map((entry) =>
						entry.results && entry.results.length >= task
							? entry.results[task - 1].mean
							: MAX_VAL
					)
				)
			);
		}
		const maxValue = Math.max(...maxValues);

		for (let task = 1; task <= 2; task++) {
			createElement("h2", solutions, { content: `Task ${task}` });

			const solutionList = [];
			for (let i = 0; i < count; i++) {
				const entry = Object.values(data)[i];
				solutionList.push([
					Object.keys(data)[i],
					entry.results && entry.results.length >= task
						? entry.results[task - 1].mean
						: undefined,
					entry.valid,
				]);
			}
			solutionList.sort((a, b) => a[1] - b[1]);

			for (const [name, mean, valid] of solutionList) {
				const solution = createElement("div", solutions, {
					classes: [
						"solution",
						valid == "false" || mean == undefined
							? "invalid"
							: undefined,
					],
				});
				createElement("div", solution, {
					classes: ["name"],
					content: name,
				});
				const timeBar = createElement("div", solution, {
					classes: ["bar"],
				});
				createElement("div", timeBar, {
					classes: ["bar-title"],
					content: "Time",
				});
				const innerBar = createElement("div", timeBar, {
					classes: ["bar-inner"],
				});

				if (mean != undefined) {
					const percent = (mean / maxValue) * 100;
					createFilledBar(innerBar, percent);
					createElement("div", timeBar, {
						classes: ["bar-time"],
						content: `${mean.toFixed(4)} ms`,
					});
				}
			}
		}
	}
}

function createFilledBar(parent, percent) {
	const part1 = createElement("div", parent, {
		classes: ["bar-part", "part-1"],
	});
	part1.style.width = `${percent}%`;
	// const part2 = createElement("div", parent, {
	// 	classes: ["bar-part", "part-2"],
	// });
}

prepareDays();
loadDays();
