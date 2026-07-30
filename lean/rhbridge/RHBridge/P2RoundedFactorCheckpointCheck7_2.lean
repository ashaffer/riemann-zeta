import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk2 :
    P2RoundedFactorCheckpointData.panel7Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix8_eq :
    P2RoundedFactorCheckpointData.panel7Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk2.1

theorem panel7Prefix9_eq :
    P2RoundedFactorCheckpointData.panel7Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk2.2.1

theorem panel7Prefix10_eq :
    P2RoundedFactorCheckpointData.panel7Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk2.2.2.1

theorem panel7Prefix11_eq :
    P2RoundedFactorCheckpointData.panel7Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk2.2.2.2

end RHP2Bridge
