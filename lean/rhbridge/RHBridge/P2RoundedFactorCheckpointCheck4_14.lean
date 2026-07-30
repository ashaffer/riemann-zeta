import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk14 :
    P2RoundedFactorCheckpointData.panel4Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix56_eq :
    P2RoundedFactorCheckpointData.panel4Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk14.1

theorem panel4Prefix57_eq :
    P2RoundedFactorCheckpointData.panel4Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk14.2.1

theorem panel4Prefix58_eq :
    P2RoundedFactorCheckpointData.panel4Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk14.2.2.1

theorem panel4Prefix59_eq :
    P2RoundedFactorCheckpointData.panel4Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk14.2.2.2

end RHP2Bridge
