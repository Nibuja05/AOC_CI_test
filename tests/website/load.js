const zeroPad = (num, places) => String(num).padStart(places, "0");

// const BASE_PATH ="file:///C:/Users/anton/Programmieren/AOC_CI_test/tests/website/";
const BASE_PATH = "https://nibuja05.github.io/AOC_CI_test/";

async function loadDataForDay(day) {
	try {
		const request = await fetch(BASE_PATH + `data/${zeroPad(day, 2)}.json`);
		return await request.json();
	} catch (error) {
		console.log(error);
		console.log(`No existing data for ${day}`);
	}
	return undefined;
}

async function loadDays() {
	loadDataForDay(2);
	// for (let i = 1; i <= 24; i++) {
	// 	dayData = loadDataForDay(i);

	// 	createDay(i, dayData);
	// }
}

function createDay(index, data) {
	const nav = document.getElementById("nav");
	const newDay = document.createElement("div");
	newDay.classList.add("day");
	nav.appendChild(newDay);
	const dayLink = document.createElement("a");
	dayLink.href = `day${index}`;
	dayLink.innerHTML = index;
	newDay.appendChild(dayLink);

	if (!data) newDay.classList.add("inactive");
}

loadDays();
