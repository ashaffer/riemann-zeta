import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel13FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel13FlatComponentChunk26

end RHP2Bridge
