import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk14 :
    P2RoundedFactorCheckpointData.panel10Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix56_eq :
    P2RoundedFactorCheckpointData.panel10Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk14.1

theorem panel10Prefix57_eq :
    P2RoundedFactorCheckpointData.panel10Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk14.2.1

theorem panel10Prefix58_eq :
    P2RoundedFactorCheckpointData.panel10Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk14.2.2.1

theorem panel10Prefix59_eq :
    P2RoundedFactorCheckpointData.panel10Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk14.2.2.2

end RHP2Bridge
