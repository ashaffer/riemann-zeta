import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel21FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel21FlatComponentChunk42

end RHP2Bridge
