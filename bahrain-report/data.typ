
#let usd_oku_en(data) = {
  let USD_TO_OKU_YEN = 0.00000156
  data
    .map(x => {
      let clean = x.replace(",", "").trim()
      if clean != "" {
        float(clean) * USD_TO_OKU_YEN
      }
    })
    .filter(v => v != none)
}

// ----- Figure Styling: -----------------------------------


#let framify(object) = rect(object, stroke: orange)

// ----- Data ----------------------------------------------
#let dates = csv("data/dates_prod.csv", row-type: dictionary)
#let fruits = csv("data/fruits_prod.csv", row-type: dictionary)
#let pop = csv("data/world_population.csv").filter(data => data.at(0) in ("Country Name", "Bahrain"))
#let gdp = csv("data/gdp.csv").filter(data => data.at(0) in ("Country Name", "Bahrain"))
#let gdpcap = csv("data/gdpcap.csv").filter(data => data.at(0) in ("Country Name", "Bahrain"))
#let gvacp = csv("data/gvacp.csv")
