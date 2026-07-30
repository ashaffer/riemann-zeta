import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel26FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel26FlatComponentChunk27

end RHP2Bridge
