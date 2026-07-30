import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel13FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel13FlatComponentChunk46

end RHP2Bridge
