import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel26FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel26FlatComponentChunk41

end RHP2Bridge
