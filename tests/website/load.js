const zeroPad = (num, places) => String(num).padStart(places, "0");

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
		const newDay = document.createElement("div");
		newDay.classList.add("day");
		newDay.id = `nav-day${i}`;
		nav.appendChild(newDay);
		const dayLink = document.createElement("a");
		dayLink.href = `#day${i}`;
		dayLink.innerHTML = i;
		newDay.appendChild(dayLink);

		newDay.classList.add("inactive");
	}
}

function createDay(index, data) {
	const newDay = document.getElementById(`nav-day${index}`);

	if (data && Object.keys(data).length > 0) {
		newDay.classList.remove("inactive");

		const resultContainer = document.getElementById("content");
		const result = document.createElement("div");
		result.classList.add("result");
		result.id = `day${index}-data`;
		resultContainer.appendChild(result);
		const anchor = document.createElement("div");
		anchor.classList.add("anchor");
		anchor.id = `day${index}`;
		result.appendChild(anchor);

		const header = document.createElement("h2");
		header.innerHTML = `Day ${index}`;
		result.appendChild(header);
	}
}

prepareDays();
loadDays();
