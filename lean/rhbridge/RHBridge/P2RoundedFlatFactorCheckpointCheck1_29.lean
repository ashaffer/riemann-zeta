import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel1FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel1FlatComponentChunk29

end RHP2Bridge
