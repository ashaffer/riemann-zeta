import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel21FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel21FlatComponentChunk25

end RHP2Bridge
