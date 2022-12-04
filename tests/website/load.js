const zeroPad = (num, places) => String(num).padStart(places, "0");

function loadDays() {
	for (let i = 1; i <= 24; i++) {
		dayData = {};
		const t = import("../data/01.json");
		try {
			dayData = require(`../data/${zeroPad(i, 2)}.json`);
		} catch (error) {
			console.log("not existing: ", i);
		}
	}
}

loadDays();
