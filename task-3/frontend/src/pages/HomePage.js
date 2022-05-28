import React, {useContext} from "react"
import AuthContext from "../context/AuthContext"

const HomePage = () => {
    const {name} = useContext(AuthContext)
    return (
        <div>
            Hello {name}
        </div>
    )
}

export default HomePage