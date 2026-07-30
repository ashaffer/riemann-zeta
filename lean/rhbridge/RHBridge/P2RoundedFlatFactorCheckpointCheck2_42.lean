import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel2FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel2FlatComponentChunk42

end RHP2Bridge
