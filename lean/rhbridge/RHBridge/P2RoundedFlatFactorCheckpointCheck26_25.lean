import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel26FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel26FlatComponentChunk25

end RHP2Bridge
