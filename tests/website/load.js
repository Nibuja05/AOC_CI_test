const zeroPad = (num, places) => String(num).padStart(places, "0");

// const BASE_PATH ="file:///C:/Users/anton/Programmieren/AOC_CI_test/tests/website/";
const BASE_PATH =
	"file:///C:/Users/anton/Programmieren/AOC_CI_test/tests/website/";

async function loadDataForDay(day) {
	// return {};
	const request = await fetch(BASE_PATH + `data/${zeroPad(day, 2)}.json`);
}

async function loadDays() {
	for (let i = 1; i <= 24; i++) {
		dayData = {};
		// const t = import(BASE_PATH + "../data/01.json");

		try {
			dayData = loadDataForDay(i);
		} catch (error) {
			console.log("not existing: ", i);
		}
	}
}

loadDays();
