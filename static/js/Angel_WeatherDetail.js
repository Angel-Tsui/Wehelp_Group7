const weatherDetail = document.querySelector(".content__weatherDetail")

// 總覽
const detailOverview = document.createElement("div")
detailOverview.className = "content__weatherDetail--overview"
weatherDetail.appendChild(detailOverview)

// 總覽 > 圖片
const overviewImg = document.createElement("div")
let img = "/static/images/lightning.png";
overviewImg.style.backgroundImage = 'url(' + img + ')'
overviewImg.className = "overview__img";
detailOverview.appendChild(overviewImg)

// 總覽 > 資料
const overviewInfo = document.createElement("div");
overviewInfo.className = "overview__info"
detailOverview.appendChild(overviewInfo)

// 總覽 > 資料 > 名字
const infoAreaName = document.createElement("div");
infoAreaName.className = "info__areaName";
infoAreaName.innerText = "臺北市";
overviewInfo.appendChild(infoAreaName)

// 總覽 > 資料 > 細節
const infoDetail = document.createElement("div");
infoDetail.className = "info__Detail";
overviewInfo.appendChild(infoDetail)

// 總覽 > 資料 > 細節 > 氣溫
const infoTemp = document.createElement("div");
infoTemp.id = "info__temp";
infoTemp.className = "title"
infoTemp.innerHTML = `<div>氣溫<br/><span></span></div>`;
infoDetail.appendChild(infoTemp)
const infoTemp_span = document.querySelector("#info__temp span");
infoTemp_span.className = "content"
infoTemp_span.innerText = "25° - 30°"

// 總覽 > 資料 > 細節 > 降雨量
const infoRain = document.createElement("div");
infoRain.id = "info__Rain";
infoRain.className = "title"
infoRain.innerHTML = `<div>降雨量<br/><span></span></div>`;
infoDetail.appendChild(infoRain);
const infoRain_span = document.querySelector("#info__Rain span");
infoRain_span.className = "content"
infoRain_span.innerText = "10%"

// 白天

// 晚上