import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk2 :
    P2RoundedFactorCheckpointData.panel13Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix8_eq :
    P2RoundedFactorCheckpointData.panel13Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk2.1

theorem panel13Prefix9_eq :
    P2RoundedFactorCheckpointData.panel13Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk2.2.1

theorem panel13Prefix10_eq :
    P2RoundedFactorCheckpointData.panel13Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk2.2.2.1

theorem panel13Prefix11_eq :
    P2RoundedFactorCheckpointData.panel13Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk2.2.2.2

end RHP2Bridge
