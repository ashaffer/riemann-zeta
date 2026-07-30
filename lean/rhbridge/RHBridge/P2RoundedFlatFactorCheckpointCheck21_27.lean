import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel21FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel21FlatComponentChunk27

end RHP2Bridge
