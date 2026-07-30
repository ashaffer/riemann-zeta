import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel21FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel21FlatComponentChunk38

end RHP2Bridge
