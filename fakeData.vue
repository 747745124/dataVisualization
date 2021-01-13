<template>
  <div id="fakeData" :style="{ width: 600, height: 600 }"></div>
</template>
<script>

export default {
  name: "Sunburst",data: [
    {
    virusData: [
            {name:'Bronx',infected: 73371,death: 123,cured: 23313
            },
            {name:'Manhattan',infected: 24427,death: 109,cured: 12241
            },
            {name:'Queens',infected: 3512,death: 22,cured: 1234
            },
            {name:'Brooklyn',infected: 23441,death: 121,cured: 6632
            },
            {name:'Staten Island',infected: 11223,death: 231,cured: 5532
            }
        ],
    week: 1,
    twitter: {
    topTwitter:'Make America Great Again!',
    total: 3220,
    moodIndex: 0.38,
    topic: ['virus','election','lockdown'
            ]
        }
    },
    {
    virusData: [
            {name:'Bronx',infected: 73371,death: 123,cured: 23313
            },
            {name:'Manhattan',infected: 24427,death: 109,cured: 12241
            },
            {name:'Queens',infected: 3512,death: 22,cured: 1234
            },
            {name:'Brooklyn',infected: 23441,death: 121,cured: 6632
            },
            {name:'Staten Island',infected: 11223,death: 231,cured: 5532
            }
        ],
    week: 2,
    twitter: {
    topTwitter:'How dare you!',
    total: 3002,
    moodIndex: 0.26,
    topic: ['Vaccine','KanyeIsOverParty','ImpeachmentDay'
            ]
        }
    },
]

}