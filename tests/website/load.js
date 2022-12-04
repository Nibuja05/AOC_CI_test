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
	// loadDataForDay(1);
	for (let i = 1; i <= 24; i++) {
		dayData = await loadDataForDay(i);

		createDay(i, dayData);
	}
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

	if (data && Object.keys(data).length > 0) {
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

		console.log(data);
		createElement;

		// const
	}
}

prepareDays();
loadDays();
