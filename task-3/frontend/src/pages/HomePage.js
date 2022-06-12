import React, {useContext} from "react"
import AuthContext from "../context/AuthContext"
import { DataPage } from "./DataPage"

export const HomePage = () => {
    return (
        <div>
            <DataPage />
        </div>
    )
}