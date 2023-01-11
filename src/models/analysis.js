import {Schema,model} from 'mongoose';

const formSchema = new Schema({
    patient:{
        type: Schema.Types.ObjectId,
        required: true,
        ref:"patient"
    },
    dateOfanalysis:{
        type: Date,
        required: true,
        default: Date.now
    },
    focusOfInfection:{
        type: String,
        required: true
    },
    infection: {
        UTI: {
          type: Boolean,
          required: true
        },
        CNS: {
          type: Boolean,
          required: true
        },
        skinAndSoftTissue: {
            type: Boolean,
            required: true
        },
        abdominal: {
          type: Boolean,
          required: true
        },
        bacteremia: {
          type: Boolean,
          required: true
        },
        pneumonia: {
            type: Boolean,
            required: true
        },
        catheter_Lines_Stents:{
            type: Boolean,
            required: true
        },
        others: {
          type: String,
          required: false
        },
        required: true
      },
      specimen:{
        type: [String], // for multiple option List 
        required: true,
        enum:["Blood","Sputum","Urine","CSF","Wound","Pus","BAL","Stool","Mini Bal","Others","Ascetic fluid","Pleural fluid","Tissue"],
        default: null
      },
      organism:{
        type:String,
        required:true
      },
      antibioticAccordingtoCulture:{
        type:Boolean,
        required:true,
        default:false
      },
      antibioticGiven:{
        type:String,
        required:false
      },
      rightIndication:{

      },
      rightDrug:{

      },
      rightDose:{
        loadingDose:{
          type:Boolean,
        required:true,
        default:false
        },
        maintenanceDose:{
          type:Boolean,
        required:true,
        default:false
        },
      },
      rightFrequency:{
        type:Boolean,
        required:true,
        default:false
      },
      rightDuration:{
        type:Boolean,
        required:true,
        default:false
      },
      totalScore:{
        type:Number,
        required:true,
        default:0
      },
      appropriatness:{
        type:Boolean,
        required:true,
      },
      rightDocumentation:{
        type:Boolean,
        required:false,
        default:false
      },
      recommendationField:{
        type:Boolean,
        default:null
      },
      outcome:{
        type:String,
        enum:["DEATH","ALIVE"],
        default:"Alive"
      },
      antibioticChanged:{
        type:Boolean,
        default:false,
      },
      antibioticDoseChanged:{
        type:Boolean,
        default:false,
      },
      serumCreatinine:{
        type:Number,
        default:null,
        required:false
      },
      duration:{
        type:Number,
      },
      recommendation:[{
        indication:{
          type:Boolean,
          default:null
        },
        drug:{
          type:Boolean,
          default:null
        },
        dose:{
          type:Boolean,
          default:null
        },
        frequency:{
          type:Boolean,
          default:null
        },
        duration:{
          type:Boolean,
          default:null
        }
      }],
      comments:{
        type:String,
        default:null,
        required:false
      },


},{timestamps:true});

const Analysis=model('analysis',formSchema);

export default Analysis;