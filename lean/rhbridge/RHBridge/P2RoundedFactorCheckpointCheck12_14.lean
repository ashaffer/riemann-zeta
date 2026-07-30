import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk14 :
    P2RoundedFactorCheckpointData.panel12Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix56_eq :
    P2RoundedFactorCheckpointData.panel12Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk14.1

theorem panel12Prefix57_eq :
    P2RoundedFactorCheckpointData.panel12Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk14.2.1

theorem panel12Prefix58_eq :
    P2RoundedFactorCheckpointData.panel12Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk14.2.2.1

theorem panel12Prefix59_eq :
    P2RoundedFactorCheckpointData.panel12Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk14.2.2.2

end RHP2Bridge
