import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel1FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel1FlatComponentChunk36

end RHP2Bridge
