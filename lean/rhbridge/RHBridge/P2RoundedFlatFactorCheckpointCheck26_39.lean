import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel26FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel26FlatComponentChunk39

end RHP2Bridge
