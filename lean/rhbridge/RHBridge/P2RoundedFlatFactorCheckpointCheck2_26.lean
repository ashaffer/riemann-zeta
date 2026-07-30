import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel2FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel2FlatComponentChunk26

end RHP2Bridge
