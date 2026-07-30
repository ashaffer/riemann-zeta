import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk2 :
    P2RoundedFactorCheckpointData.panel9Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix8_eq :
    P2RoundedFactorCheckpointData.panel9Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk2.1

theorem panel9Prefix9_eq :
    P2RoundedFactorCheckpointData.panel9Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk2.2.1

theorem panel9Prefix10_eq :
    P2RoundedFactorCheckpointData.panel9Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk2.2.2.1

theorem panel9Prefix11_eq :
    P2RoundedFactorCheckpointData.panel9Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk2.2.2.2

end RHP2Bridge
