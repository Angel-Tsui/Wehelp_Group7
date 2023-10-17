const weatherDetail = document.querySelector(".content__weatherDetail")
const detailOverview = document.createElement("div")
detailOverview.className = "content__weatherDetail--overview"
weatherDetail.appendChild(detailOverview)

const overviewImg = document.createElement("div")
let img = "/static/images/lightning.png"
overviewImg.style.backgroundImage = 'url(' + img + ')'
overviewImg.className = "overview__img";
weatherDetail.appendChild(overviewImg)

const overviewInfo = document.createElement("div");
overviewInfo.className = "overview__info"
weatherDetail.appendChild(overviewInfo)