import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel2FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel2FlatComponentChunk41

end RHP2Bridge
