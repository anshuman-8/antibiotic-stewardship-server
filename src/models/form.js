import {Schema,model} from 'mongoose';

const formSchema = new Schema({
    patient:{
        type: Schema.Types.ObjectId,
        required: true,
        ref:"patient"
    },
    dateOfReview:{
        type: Date,
        required: true,
        default: Date.now
    },
    reviewingDepartment:{
        type: String,
        required: true
    },
    cultureSent:{
        type: Boolean,
        required: true
    },
    CultureSentBeforeAntibiotics:{
        type: Boolean,
        required: true
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
      antibioticSensitive:{
        AMX_CLAV:{
          type:Boolean,
          required:true,
          default:null
        },
        AMP:{
          type:Boolean,
          required:true,
          default:null
        },
        GEN:{
          type:Boolean,
          required:true,
          default:null
        },
        COTRI:{
          type:Boolean,
          required:true,
          default:null
        },
        CIP:{
          type:Boolean,
          required:true,
          default:null
        },
        CLOX:{
          type:Boolean,
          required:true,
          default:null
        },
        CFX:{
          type:Boolean,
          required:true,
          default:null
        },
        TET:{
          type:Boolean,
          required:true,
          default:null
        },
        LEV:{
          type:Boolean,
          required:true,
          default:null
        },
        DOXY:{
          type:Boolean,
          required:true,
          default:null
        },
        NOR:{
          type:Boolean,
          required:true,
          default:null
        },
        PEN:{
          type:Boolean,
          required:true,
          default:null
        },
        ERY:{
          type:Boolean,
          required:true,
          default:null
        },
        LIN:{
          type:Boolean,
          required:true,
          default:null
        },
        VAN:{
          type:Boolean,
          required:true,
          default:null
        },
        IMP:{
          type:Boolean,
          required:true,
          default:null
        },
        MOX:{
          type:Boolean,
          required:true,
          default:null
        },
        CTX:{
          type:Boolean,
          required:true,
          default:null
        },
        CEFTZDM:{
          type:Boolean,
          required:true,
          default:null
        },
        CEFIPIME:{
          type:Boolean,
          required:true,
          default:null
        },
        AMK:{
          type:Boolean,
          required:true,
          default:null
        },
        OF:{
          type:Boolean,
          required:true,
          default:null
        },
        PIP:{
          type:Boolean,
          required:true,
          default:null
        },
        PIP_TAZ:{
          type:Boolean,
          required:true,
          default:null
        },
        CEF_SUB:{
          type:Boolean,
          required:true,
          default:null
        },
        MEM:{
          type:Boolean,
          required:true,
          default:null
        },
        CHL:{
          type:Boolean,
          required:true,
          default:null
        },
        TICAR_CALV:{
          type:Boolean,
          required:true,
          default:null
        },
        ERTA:{
          type:Boolean,
          required:true,
          default:null 
        },
        COL:{
          type:Boolean,
          required:true,
          default:null
        },
        TGC:{
          type:Boolean,
          required:true,
          default:null
        },
        RIF:{
          type:Boolean,
          required:true,
          default:null
        },
        TEICO:{
          type:Boolean,
          required:true,
          default:null
        },
        TOB:{
          type:Boolean,
          required:true,
          default:null
        },
        AZTREO:{
          type:Boolean,
          required:true,
          default:null
        },
        NF:{
          type:Boolean,
          required:true,
          default:null
        },
        CEFOTAXIME:{
          type:Boolean,
          required:true,
          default:null
        },
        AZITHRO:{
          type:Boolean,
          required:true,
          default:null
        },
        FLUCO:{
          type:Boolean,
          required:true,
          default:null
        },
        AMPHO:{
          type:Boolean,
          required:true,
          default:null
        },
        CLINDA:{
          type:Boolean,
          required:true,
          default:null
        },
        MICA:{
          type:Boolean,
          required:true,
          default:null
        },
        ANIDUL:{
          type:Boolean,
          required:true,
          default:null
        },
        CASPO:{
          type:Boolean,
          required:true,
          default:null
        },
        OXAC:{
          type:Boolean,
          required:true,
          default:null
        },
        DAPTO:{
          type:Boolean,
          required:true,
          default:null
        },
        MDR:{
          type:String,
          enum:["MDR","No MDR","PS",null],
          default:null
        },
        resistance:{
          type:String,
          enum:["Col Re","VRE","MRSA","ESBL","CRE",null],
        },
        required: false
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

const Form=model('form',formSchema);

export default Form;