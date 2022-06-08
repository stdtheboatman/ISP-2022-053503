import React, {useContext} from "react"
import AuthContext from "../context/AuthContext"

export const UpdateUserDataPage = () => {
    const {updateUserData} = useContext(AuthContext)
    return (
    <div>
        <form onSubmit={updateUserData}>
            <input type="text" name="apiKey" placeholder="Enter api key" />
            <input type="text" name="secretKey" placeholder="Enter secret key" />
            <input type="submit" />            
        </form>
    </div>
  )
}
