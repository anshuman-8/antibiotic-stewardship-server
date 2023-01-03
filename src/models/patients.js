import {Schema, model} from 'mongoose';

const PatientSchema = new Schema({
    name:{
        type: String,
        required: true
    },
    MRDNumber:{
        type: String,
        required: true
    },
    dateOfAdmission:{
        type: Date,
        required: true,
        default: Date.now
    },
    location:{
        type:String,
        enum:["ICU","Ward"],
        default:"Ward",
        required:false
    },
    sex:{
        type: String,
        enum:["M","F"],
        required: true
    },
    dateOfBirth:{
        type: Date,
        required: true
    },
    height:{
        type: Number,
        required: false
    },
    weight:{
        type: Number,
        required: false
    },
    placeOfResidence:{
        type: String,
        required: false
    },
    admittingDoctor:{
        type: String,
        required: false,
    },
    form:{
        type: Schema.Types.ObjectId,
        required: false,
        ref:"form"
    },
    admittingDepartment:{
        type: String,
        required: false
    },
    admittingDiagnostic:{
        type: String,
        required: false
    }
},{timestamps:true});

const Patient = model('patient', PatientSchema);

export default Patient;
