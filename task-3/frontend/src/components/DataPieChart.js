import React from "react";
import { useContext } from "react";
import { VictoryLabel, VictoryPie } from "victory";
import AuthContext from "../context/AuthContext";

const data = [
  { label: "Group A", y: 400 },
  { label: "Group B", y: 300 },
  { label: "Group C", y: 300 },
  { label: "Group D", y: 200 }
];

export const DataPieChart = () => {
    const {chartPieData} = useContext(AuthContext)

    console.log("DataPieChart")
    console.log(data)
    console.log(chartPieData)

    return (
        <div>

        {chartPieData && 
            <VictoryPie
            colorScale={["tomato", "orange", "gold", "cyan", "navy" ]}
            height={200}
            data={chartPieData.map((item, index) => {
                return {
                    label: item.symbol + "\n" + item.rate,
                    y: item.rate * 100,
                    x: index
                }

            })}
            style={{
                labels: {
                    fontSize: 4
                }
            }}
            />
        }
        </div>
    )
}
