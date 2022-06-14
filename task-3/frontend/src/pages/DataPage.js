import React, { useContext, useState } from 'react'
import { DataPieChart } from '../components/DataPieChart'
import AuthContext from '../context/AuthContext'

export const DataPage = () => {
    const {getCurrencyDistribution} = useContext(AuthContext)
    const [data, setData] = useState(null)

    const onClick = async (event) => {
        setData(await getCurrencyDistribution(event))
        console.log(1)
    }

    return (
        <div> 
            <DataPieChart />
        </div>
        
    )
}
