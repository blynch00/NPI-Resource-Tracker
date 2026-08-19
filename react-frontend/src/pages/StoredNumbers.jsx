import { SavedTable } from "../components/SavedTable"
export function StoredNumbers(){
    return (
        <div className="container">
            <header className="page-header">
                <h1>Personal Lists Here</h1>
            </header>
            <div className="page-content">
                <SavedTable/>
            </div>
        </div>
        
    )
}