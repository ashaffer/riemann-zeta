import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel2FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel2FlatComponentChunk33

end RHP2Bridge
