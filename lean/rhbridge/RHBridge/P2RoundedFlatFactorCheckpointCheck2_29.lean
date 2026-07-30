import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel2FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel2FlatComponentChunk29

end RHP2Bridge
